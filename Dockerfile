# Step 1:
# Pull image base
FROM python:3.7.13
# Step 2:
# Create environment args and variables
ARG JMETER_VERSION="5.5"
ARG CMDRUNNER_JAR_VERSION="2.2.1"
ARG JMETER_PLUGINS_MANAGER_VERSION="1.6"
ENV JMETER_HOME /opt/apache-jmeter-${JMETER_VERSION}
ENV JMETER_LIB_FOLDER ${JMETER_HOME}/lib/
ENV JMETER_PLUGINS_FOLDER ${JMETER_LIB_FOLDER}ext/
ARG USER_GIT
ARG PASS_GIT
ARG URL_PERF
ARG USER_PERF
ARG PASS_PERF
ARG ARGS
ARG PARAMS
ARG PROJNAME
ARG APPNAME
ARG VERSION
ENV ENV_ARGS=${ARGS}
ENV ENV_PARAMS=${PARAMS}
ENV ENV_PROJNAME=${PROJNAME}
ENV ENV_APPNAME=${APPNAME}
ENV ENV_VERSION=${VERSION}
# Step 3:
# Install gnupg
WORKDIR ${JMETER_HOME}
RUN  apt-get -y update \
&& apt-get install -y wget gnupg curl
# Step 4:
# Download Apache JMeter
RUN wget https://downloads.apache.org//jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz
RUN tar -xzf apache-jmeter-${JMETER_VERSION}.tgz
RUN mv apache-jmeter-${JMETER_VERSION}/* /opt/apache-jmeter-${JMETER_VERSION}
RUN rm -r /opt/apache-jmeter-${JMETER_VERSION}/apache-jmeter-${JMETER_VERSION}
# Step 5:
# Install openjdk
RUN apt update \
&& apt install -y default-jre
# Step 6:
# Download Command Runner and move it to lib folder
WORKDIR ${JMETER_LIB_FOLDER}
RUN wget https://repo1.maven.org/maven2/kg/apc/cmdrunner/${CMDRUNNER_JAR_VERSION}/cmdrunner-${CMDRUNNER_JAR_VERSION}.jar
# Step 7:
# Download JMeter Plugins manager and move it to lib/ext folder
WORKDIR ${JMETER_PLUGINS_FOLDER}
RUN wget https://repo1.maven.org/maven2/kg/apc/jmeter-plugins-manager/${JMETER_PLUGINS_MANAGER_VERSION}/jmeter-plugins-manager-${JMETER_PLUGINS_MANAGER_VERSION}.jar
# Step 8:
# Download jmeter plugins
WORKDIR ${JMETER_LIB_FOLDER}
RUN java  -jar cmdrunner-2.2.1.jar --tool org.jmeterplugins.repository.PluginManagerCMD install-all-except jpgc-hadoop,jpgc-oauth,ulp-jmeter-autocorrelator-plugin,ulp-jmeter-videostreaming-plugin,ulp-jmeter-gwt-plugin,tilln-iso8583
# Step 9:
WORKDIR ${JMETER_HOME}
# Step 10:
# Update PATH
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:${PATH}"
RUN update-ca-certificates
# Step 11:
# Copy automation tool to container
ENV AUTOMATION_HOME=/opt/automation_tool
WORKDIR ${AUTOMATION_HOME}
COPY . ${AUTOMATION_HOME}
RUN rm Dockerfile
# Step 12:
# Update PATH
ENV PATH="$AUTOMATION_HOME/bin:${JMETER_HOME}/bin:${PATH}"
WORKDIR /
# Step 13
# Install GIT
RUN apt-get install git
# Step 14
# Install and configure performance explorer CLI
RUN pip install --no-cache-dir --upgrade "git+https://${USER_GIT}:${PASS_GIT}@github.com/pslcorp/psl-performance-cli@v1.14.0#egg=psl-perfexp"
RUN psl-perfexp configure -url "${URL_PERF}" -usr "${USER_PERF}" -pass "${PASS_PERF}"
RUN psl-perfexp login
# Step 15
# Execute tests
CMD ["sh", "-c", "automate.sh"]