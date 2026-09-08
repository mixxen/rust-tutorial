# Pinned Rust release, not a moving 'latest' toolchain. OS packages can update.
FROM rust:1.90.0-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends make g++ python3 git ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && rustup component add rustfmt clippy

ARG USER_UID=1000
ARG USER_GID=1000
RUN groupadd --gid "${USER_GID}" learner \
    && useradd --uid "${USER_UID}" --gid "${USER_GID}" --create-home --shell /bin/bash learner \
    && chown -R learner:learner /usr/local/cargo /usr/local/rustup
USER learner
WORKDIR /workspace
CMD ["bash"]
