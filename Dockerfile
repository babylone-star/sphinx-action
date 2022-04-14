FROM sphinxdoc/sphinx:2.4.4

LABEL "maintainer"="Ammar Askar <ammar@ammaraskar.com>"


RUN apt-get update -y --allow-releaseinfo-change && apt-get install git -y
ADD entrypoint.py /entrypoint.py
ADD sphinx_action /sphinx_action

ENTRYPOINT ["/entrypoint.py"]
