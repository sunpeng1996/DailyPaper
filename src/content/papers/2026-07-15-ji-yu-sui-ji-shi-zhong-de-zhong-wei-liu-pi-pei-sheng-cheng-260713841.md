---
title: Heavy-Tailed Flow Matching via Random Clocks
title_zh: 基于随机时钟的重尾流匹配生成框架
authors:
- Zhouhao Yang
- Yezhen Wang
- Kenji Kawaguchi
- Vladimir Braverman
- Haoyang Cao
affiliations:
- Johns Hopkins University
- National University of Singapore
arxiv_id: '2607.13841'
url: https://arxiv.org/abs/2607.13841
pdf_url: https://arxiv.org/pdf/2607.13841
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: 生成式模型训练 · 重尾分布适配
tags:
- Flow Matching
- Heavy-tailed Data
- Generative Model
- Long-tailed Distribution
- Logsignature
one_liner: 提出随机时钟编码的重尾流匹配方法，提升重尾分布生成质量并支持可控尾部调节
practical_value: '- 长尾推荐的生成式召回场景可复用随机时钟混合高斯的思路，替代纯高斯噪声输入，提升小众商品/冷启样本的生成覆盖率

  - 可控尾部调节设计可迁移到广告转化预估的极端样本建模，仅调整尾部参数即可适配不同行业的转化分布特性

  - 截断logsignature编码路径信息的trick开销极低，可直接嵌入现有生成式推荐的流匹配/扩散模型pipeline，无需大幅改架构'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有流匹配、扩散类生成模型默认采用高斯源分布，与长尾推荐、金融极端事件等重尾场景的归纳偏置匹配度低，无法有效还原稀有尾部样本的真实分布特性。
### 方法关键点
1. 提出HTFM框架，将重尾源分布建模为随机时钟条件下的高斯分布混合，边际化时钟后可覆盖高斯、α-stable、Student-t等多种分布族；
2. 采用截断logsignature特征编码路径型随机时钟，仅增加可忽略的计算开销即可让速度场适配条件空间；
3. 支持仅调整时钟分布或尾部参数，即可灵活控制生成样本的尾部厚重程度。
### 关键结果
在2D不平衡α-stable混合数据集、CIFAR10-LT、HRRR气象数据集上，相比高斯流匹配及主流重尾基线，模式覆盖率、样本质量、尾部统计还原度均有明显提升，同时保留流匹配低NFE采样的优势。
