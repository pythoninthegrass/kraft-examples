FROM node:18-alpine AS build

RUN set -xe; \
    apk --no-cache add openssl3;

WORKDIR /app

COPY ./package.json /app/

RUN set -xe; \
    npm install;

COPY ./webpack.config.js /app/
COPY ./src /app/src
COPY ./prisma /app/prisma

RUN set -xe; \
    npx prisma generate; \
    npx prisma migrate deploy; \
    npx prisma db seed; \
    npm run build \
    ;

FROM scratch

# Distribution configuration
COPY --from=build /etc/os-release /etc/os-release

# Library files
COPY --from=build /usr/lib/libcrypto.so.3 /lib/libcrypto.so.3
COPY --from=build /usr/lib/libssl.so.3 /lib/libssl.so.3

# rest-express + Prisma
COPY --from=build /app/dist /usr/src
