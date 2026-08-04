---
title: 'Auditing Semantic Gains in Sequential Recommendation: A Lightweight Recovery
  Test'
title_zh: 序列推荐语义增益审计：轻量级可解释恢复测试框架LIME-Rec
authors:
- Kong Wang
- Zhongke He
- Xiang Chen
- Hongwei Zeng
- Kai Deng
- Long Wang
- Kehua Yang
affiliations:
- Hunan University
- Dalian University of Technology
- Tongji University
- University of Chinese Academy of Sciences
- Beihang University
arxiv_id: '2608.01260'
url: https://arxiv.org/abs/2608.01260
pdf_url: https://arxiv.org/pdf/2608.01260
published: '2026-08-02'
collected: '2026-08-04'
category: RecSys
direction: 序列推荐 · 语义增益归因审计
tags:
- Sequential Recommendation
- Semantic Recommendation
- Score Fusion
- Attribution Analysis
- Lightweight Model
one_liner: 通过三专家可解释分数融合复现语义推荐增益，无需在线LLM推理，可定位增益来源
practical_value: '- 可直接复用三专家（SASRec+ItemCF+离线语义embedding）分数融合架构，无需在线LLM推理即可获得7%~12%的R@10提升，适配低延迟要求的电商推荐场景

  - 语义信号接入可直接用通用预训练文本编码器（如BGE、MiniLM）做离线embedding，无需针对推荐任务微调，大幅降低接入成本

  - 语义增益量化可参考论文的消融方法：随机打乱语义embedding与item ID的对应关系，即可快速计算语义信号的真实贡献，避免过度引入复杂语义架构

  - 可复用有界历史校准策略：对用户已交互item施加可调控的分数惩罚，适配允许重复推荐的电商/内容场景，进一步提升召回效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前语义/生成式推荐普遍宣称比纯ID基线效果更优，但增益来源存在严重归因模糊：无法区分是来自在线LLM推理、Semantic ID生成等重型架构，还是离线语义表示、多信号互补等轻量组件，导致很多业务盲目引入复杂方案后徒增推理成本和延迟，却没有获得预期收益。

### 方法关键点
- 三个独立无参数共享的专家：纯ID的SASRec序列专家、带时间衰减权重的ItemCF协同专家、基于冻结BGE编码器生成的离线item语义embedding的语义专家，三者各自输出全库打分
- 对单个用户的三个专家打分分别做min-max归一化，用仅基于用户统计特征（历史长度、各专家得分分布等）训练的线性门控做分数级融合，每个专家的贡献可独立观测审计
- 融合后增加有界历史校准：对用户已交互item施加不超过0.1的分数惩罚，适配允许重复推荐的场景
- 整个推理链路无在线LLM/文本编码操作，融合门控和校准参数仅用验证集训练，不接触测试数据

### 关键结果
在Amazon Beauty、Toys、Sports三个电商基准数据集上，对比TIGER、LC-Rec、GRAM等当前最优语义/生成式推荐基线，LIME-Rec的R@10分别达0.0996、0.1105、0.0593，相对最强基线提升7%~12%；消融实验显示三专家融合贡献了60%以上的增益，历史校准仅贡献约30%；随机打乱item与语义embedding的对应关系会让R@10下降13.6%~17.5%，证明增益确实来自真实语义关联而非额外参数容量。

在将语义推荐的增益归因于在线LLM推理、Semantic ID生成等重型架构之前，应先用离线语义表示+多信号轻量融合的基线排除可复现的增益，避免引入不必要的架构复杂度。
