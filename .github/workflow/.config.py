version: 2.1
jobs:
  compile:
   docker:
      - image: tyuzu/kernel:build
   steps:
      - run:
          command: |
           git config --global user.name "tzuyu-xd"
           git config --global user.email "sahruldarmian212@gmail.com"
           git clone --depth=1 https://github.com/mvaisakh/gcc-arm64.git -b gcc-master .
           git add .
           git commit -m "."
           git push
           

workflows:
  version: 2.1
  cooking:
    jobs:
      - compile
