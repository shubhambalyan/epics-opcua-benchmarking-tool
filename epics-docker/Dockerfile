FROM centos:7

MAINTAINER "S Balyan <shubham.balyan@kit.edu>"

RUN mkdir -p /foo/epics
WORKDIR /foo/epics/

RUN yum update -y && yum install -yq wget apt-transport-https
RUN yum install -y make
RUN yum groupinstall -y 'Development Tools'
RUN yum install -y procserv telnet git gcc

RUN git clone https://github.com/epics-base/epics-base.git .
RUN file="$(ls -1 /foo/epics/)" && echo $file
RUN com="$(gcc -v)" && echo $com
RUN make

ENV EPICS_BASE=/foo/epics
ENV EPICS_HOST_ARCH=linux-x86_64
ENV PATH=${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:${PATH}

EXPOSE 5064-5065 5064-5065/udp
EXPOSE 5075 5076/udp

COPY ./st.cmd /foo/epics/ioc/st.cmd
COPY ./opcuaIoc /foo/epics/ioc/opcuaIoc
COPY ./opcuaIoc.dbd /foo/epics/ioc/opcuaIoc.dbd
COPY ./db.db /foo/epics/ioc/db.db

RUN chmod +x /foo/epics/ioc/st.cmd
RUN chmod +x /foo/epics/ioc/opcuaIoc
RUN chmod +x /foo/epics/ioc/opcuaIoc.dbd
RUN chmod +x /foo/epics/ioc/db.db

WORKDIR /foo/epics/ioc/
RUN work_dir="$(pwd)" && echo $work_dir
