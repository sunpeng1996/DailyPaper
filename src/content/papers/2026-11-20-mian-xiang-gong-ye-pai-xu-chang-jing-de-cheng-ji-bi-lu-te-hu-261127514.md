---
title: Deep Cross-Division Network for Product-and-Ratio Feature Interactions in Industrial
  Ranking
title_zh: 面向工业排序场景的乘积-比率特征交互深度交叉除法网络
authors:
- Mikhail Trapeznikov
- Sofia Gulevskaia
- Maksim Utushkin
- Aleksandr Poslavsky
- Alexander D'yakonov
affiliations:
- AI VK
- Lomonosov Moscow State University
arxiv_id: '2611.27514'
url: https://arxiv.org/abs/2611.27514
pdf_url: https://arxiv.org/pdf/2611.27514
published: '2026-11-20'
collected: '2026-11-23'
category: RecSys
direction: 工业推荐排序 · 特征交互建模
tags:
- Feature Interaction
- DCNv2
- Learning to Rank
- Industrial RecSys
- Ranking Optimization
one_liner: 在DCNv2基础上新增除法分支，自动学习乘积/比率特征交互，无需人工构造比率特征
practical_value: '- 可直接复用DCDN的除法分支设计替换现有排序模型中的DCNv2模块，砍掉全部人工构造的比率类衍生特征（如CTR、曝光归一化转化指标），可减少约40%的输入特征，大幅降低特征工程维护成本

  - 特征交互模块可采用分层设计：用轻量DCDN建模乘积/比率类结构化代数交互，下游接HIFORMER等通用注意力模块建模复杂异构特征关系，兼顾精度和推理效率

  - 生产部署时可对DCDN算子做Triton内核融合，实测模型推理耗时可降40%+，端到端排序服务耗时降10%+，适配高QPS的电商/广告/短视频排序场景

  - 验证了将高频重复的人工代数特征变换下沉为模型归纳偏置的思路有效，可推广到其他存在大量人工衍生特征的业务场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐排序系统中，DCN/DCNv2仅能建模非负整数阶的乘积特征交互，无法自动生成比率类特征（如CTR、转化/曝光比），必须依赖人工构造衍生特征，既增加特征工程维护成本，又抬升输入维度和推理开销，在高QPS的工业场景下性价比极低。

### 方法关键点
- 提出DCDN交叉层，在原有DCNv2的乘积交叉分支外新增锚定原始输入的倒数交叉分支，同时支持乘积、比率、混合乘积-比率三类特征交互，可表示的交互形式为多元Laurent多项式
- 落地时采用稳定倒数 `sgn(x)/max(|x|, ε)` 避免数值溢出，仅对可作为分母的特征维度开启除法分支，降低冗余计算
- 单层DCDN即可覆盖常见的两两乘积、比率交互需求，K层DCDN可生成L1阶最高K+1、符号阶在[-K, K+1]之间的Laurent单项式

### 关键结果
离线在Yambda、KuaiRec、KuaiRand、VK-LSVD4个公开推荐数据集上对比DCNv2、AFN+、EulerNet等基线：单层DCDN的nDCG@10全面优于DCNv2，推理延迟与DCNv2基本持平，比支持负阶交互的AFN+/EulerNet快6~8倍。生产落地短视频排序场景时，替换原有DCNv2模块并砍掉全部人工比率特征，输入特征减少40.1%，模型计算耗时下降42.4%，端到端排序服务耗时下降10.5%；A/B测试点赞提升3.25%、分享提升16.26%、总观看时长提升0.33%，所有指标均统计显著。

> 最值得记住：把高频重复的人工代数特征变换下沉为模型的结构化归纳偏置，可同时实现降本、提效、升指标
