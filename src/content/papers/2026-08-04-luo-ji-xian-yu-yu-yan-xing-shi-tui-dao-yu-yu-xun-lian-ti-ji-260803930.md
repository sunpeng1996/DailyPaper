---
title: 'Logic Before Language: Pre-pretraining on Formal Derivations Fosters Skill
  Acquisition and Compressibility'
title_zh: 逻辑先于语言：形式推导预预训练提升技能习得与模型可压缩性
authors:
- Jo-Ku Cheng
- Nikolaos Aletras
- Marco Valentino
affiliations:
- University of Sheffield
arxiv_id: '2608.03930'
url: https://arxiv.org/abs/2608.03930
pdf_url: https://arxiv.org/pdf/2608.03930
published: '2026-08-04'
collected: '2026-08-05'
category: Training
direction: LLM预训练 · 符号预预训练
tags:
- Pre-pretraining
- Formal Logic
- Model Compression
- Skill Acquisition
- Inductive Bias
one_liner: 基于形式逻辑推导的预预训练策略，少用36B token达80%语言任务准确率，支持33%稀疏度无损压缩
practical_value: '- 业务侧训练垂域小模型时，可先在结构化符号数据（如商品逻辑规则、用户行为范式）上做预预训练，降低后续自然语言/行为数据的训练成本，加快技能收敛

  - 针对需要部署在端侧/边缘节点的Agent、推荐小模型，可借鉴Logic-PPT思路，通过引入结构化归纳偏置降低模型表示秩，提升稀疏剪枝容错率，30%左右稀疏度下可保留基线性能

  - 对需要强推理能力的电商导购Agent、查询理解模块，可补充形式化逻辑推导任务作为预训练辅助数据，提升语义理解、组合推理的准确率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有符号预预训练方法（如Dyck语言、排序算法）依赖窄范围基元，无法捕捉自然语言的组合性、关系依赖等核心特性，且此前研究仅在<10B token的训练规模下验证效果，无法明确大训练量下的技能涌现规律与表征动态变化，亟需更具表达性的预预训练数据方案。
### 方法关键点
- 提出Logic-PPT两阶段训练框架：第一阶段在247种涵盖命题、术语、一阶逻辑的推导规则生成的2.5B符号数据上做预训练，仅保留Transformer backbone，随机初始化词表与输出头后进入第二阶段自然语言预训练
- 任务形式化为自回归的推导下一步预测，损失仅计算目标推导步的token，避免浪费模型容量在固定prompt上下文的重建
- 数据生成采用后向链式构造推导树，结合结构保留的符号重命名扩增，在保留逻辑拓扑的前提下提升数据多样性，避免过拟合表面模式
### 关键实验
在100B token FineWeb-Edu语料上训练254M参数Qwen3模型，对比随机初始化（PT）、形式语言预预训练（Formal-PPT）、算法类预预训练（Alg-PPT）三个基线：
- 语言任务达80%平均准确率比标准PT少用36B token，最终17项基础任务平均准确率87.4%，比次优基线高7.1个百分点
- 模型表征空间秩更低、频谱更集中，Wanda剪枝下33%稀疏度时性能与稠密基线持平，40%稀疏度下性能仅相对下降14.4%，远低于基线的24.7%~31.6%
### 核心结论
结构化符号归纳偏置不仅能降低大模型训练的数据成本，还能从根本上优化模型的表征几何结构，实现性能与压缩效率的双重提升
