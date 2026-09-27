---
title: X-Rec Technical Report
title_zh: X-Rec：基于流匹配的工业级连续生成式召回框架
authors:
- Chenglei Shen
- Chenzhe Huang
- Dong Jiang
- Hongjie Gao
- Jue Zhang
- Kun Xú
- Lincan Cai
- Nan Zhuang
- Pan Zhang
- Shi Chen
affiliations:
- ByteDance
arxiv_id: '2609.29180'
url: https://arxiv.org/abs/2609.29180
pdf_url: https://arxiv.org/pdf/2609.29180
published: '2026-09-24'
collected: '2026-09-27'
category: GenRec
direction: 生成式推荐 · 流匹配召回
tags:
- Generative Retrieval
- Flow Matching
- Diffusion Transformer
- Recommendation System
- Industrial Deployment
one_liner: 提出基于流匹配的连续生成式召回框架，兼顾U2I效率与SID-AR表达能力，在TikTok落地获正向收益
practical_value: '- 可复用锚点条件生成设计：将召回触发embedding生成拆解为语义区域粗选+细粒度优化，既降低生成难度，还可通过调整锚点采样温度直接控制召回多样性，适配不同业务的精准/发散需求

  - 适配召回场景的几何优化：现有工业召回embedding多经L2归一化位于超球面，直接采用黎曼流匹配替代欧氏空间扩散，无需额外约束生成结果落回流形，减少模型容量浪费，提升召回效果

  - 生成式召回工程落地核心优化：采用晚交互DiT架构，预计算用户历史序列前L-1层Transformer的KV缓存，每步去噪仅调用最后一层计算速度场，仅损失1.05pp
  Recall@20即可提升8.28倍生成吞吐量

  - 训练流程可直接迁移：先在海量用户交互序列上预训练通用序列转移模式，再针对业务场景构造正负例做SFT，比直接场景训练提升5.27pp Recall@20，大幅降低业务适配成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式召回两类主流范式均存在工业落地瓶颈：U2I检索用少量固定embedding表征用户兴趣，表达能力不足无法覆盖多峰需求；基于Semantic ID的自回归生成（SID-AR）存在量化误差，且序列解码吞吐极低，无法适配大规模召回场景。

### 方法关键点
1. 锚点条件机制：先预测目标item所属聚类锚点，再基于锚点生成最终召回触发embedding，实现粗到细的可控生成
2. 黎曼流匹配：对齐召回embedding的超球面几何结构，沿测地线构建生成轨迹，避免欧氏空间扩散导致的生成结果偏离流形问题
3. 晚交互DiT架构：用户历史序列经前L-1层Transformer预计算得到上下文表示，每步去噪仅输入最后一层做速度场估计，复用缓存降低计算量
4. 两阶段训练：先在大规模用户交互序列上预训练通用序列转移模式，再针对业务场景做监督微调适配

### 关键结果
- 离线TikTok流式benchmark：Recall@20显著优于U2I基线，与SID-AR精度相当，推理吞吐量较SID-AR高3.46×
- 在线TikTok垂类内容召回：两次上线后垂类engagement提升4.1484%，大盘engagement提升0.0111%
- 消融实验：锚点条件提升Recall@20 2.05pp，黎曼流匹配提升1.78pp，晚交互设计仅损失1.05pp Recall@20但提升8.28×吞吐量

> 值得记住：固定召回候选预算下，生成多trigger扩兴趣覆盖的收益远高于单trigger加深召回深度的收益
