---
title: Dithered Gaussian Mechanism for Randomness-Efficient Differential Privacy
title_zh: 面向随机数效率优化的抖动高斯差分隐私机制
authors:
- Nikita P. Kalinin
- Rasmus Pagh
affiliations:
- Institute of Science and Technology Austria
- University of Copenhagen
- BARC
arxiv_id: '2607.06320'
url: https://arxiv.org/abs/2607.06320
pdf_url: https://arxiv.org/pdf/2607.06320
published: '2026-07-07'
collected: '2026-07-08'
category: Other
direction: 差分隐私 · 高效随机数生成优化
tags:
- Differential Privacy
- Gaussian Mechanism
- DP-SGD
- Randomness Optimization
- Privacy Preserving
one_liner: 提出离散化输出而非噪声分布的抖动高斯机制，保留差分隐私保证的同时大幅降低高质量随机比特需求
practical_value: '- 做用户隐私合规的推荐/广告模型DP-SGD训练时，可直接替换原有高斯噪声模块，仅需极低额外开销即可避免浮点精度导致的隐私漏洞

  - 隐私敏感的用户行为数据匿名化、Semantic ID扰动等场景，可复用输出离散化思路，无需修改原有噪声分布即可实现离散DP输出

  - 需要高安全等级差分隐私落地的业务，可复用双随机源分离架构，既保证密码学级安全，又不会引入过大性能损耗'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有高斯差分隐私机制为理想连续分布，实际落地时受有限浮点精度限制易出现隐私漏洞，且生成密码学安全噪声需大量高质量随机比特，性能开销高。
### 方法关键点
1. 不对噪声分布做离散化，直接对隐私输出做抖动离散化，视为标准高斯机制的后处理，天然继承原有隐私保证，规避浮点精度导致的隐私风险
2. 拆分随机源为两类：隐私敏感的采样步骤使用高安全等级随机数，离散化步骤使用可公开的高性能随机数，即使后者被敌手获取也不影响隐私性
### 关键结果
- 所需高质量随机比特数大幅下降，且需求与噪声水平完全无关
- 落地到DP-SGD训练场景中，实现抗浮点漏洞的密码学安全噪声生成，仅带来可忽略的额外开销
