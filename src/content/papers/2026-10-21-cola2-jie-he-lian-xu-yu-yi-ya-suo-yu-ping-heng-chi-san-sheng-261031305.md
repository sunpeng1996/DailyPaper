---
title: 'Cola2: Co-Adaptive Hierarchical Language Modeling with Continuous Semantic
  Compression and Balanced Discrete Generation'
title_zh: Cola2：结合连续语义压缩与平衡离散生成的协同自适应层级语言模型
authors:
- Hongcan Guo
- Yian Zhao
- Feng Wang
- Shen Nie
- Guoqiang Wei
- Yan Zeng
- Hengshuang Zhao
affiliations:
- The University of Hong Kong
- ByteDance Seed
- Peking University
- Renmin University of China
arxiv_id: '2610.31305'
url: https://arxiv.org/abs/2610.31305
pdf_url: https://arxiv.org/pdf/2610.31305
published: '2026-10-21'
collected: '2026-10-23'
category: LLM
direction: LLM 层级语义压缩生成建模
tags:
- HierarchicalLM
- SemanticCompression
- DiffusionLM
- Co-Adaptation
- EfficientTraining
one_liner: 提出连续-离散协同自适应的层级语言建模框架，仅346B训练token性能接近Llama3-8B
practical_value: '- 长序列压缩场景（用户长行为序列、商品评价聚合）可复用动态语义分段+无辅助损失负反馈压缩率控制机制，比固定粒度压缩信息密度高20%以上

  - 生成类任务（商品文案、营销话术生成）可借鉴clean/noise/drop三态混合训练策略，平衡语义还原度与生成灵活性，无需微调即可通过CFG调节权重

  - 跨模态语义对齐场景可参考连续-离散表征协同自适应训练范式，token侧预测梯度直接更新语义编码器，避免表征与下游任务脱节

  - 低训练成本大模型落地可复用梯度解耦设计：先训语义编码器+解码器，再单独训latent扩散模型，小预算下即可达到接近千亿token预训练模型效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有层级语言生成将连续语义建模与离散文本生成割裂，固定编码器会限制表征适配解码需求，单独拟合latent先验又会让表征偏向易拟合而非对生成有用的方向，无法在有限latent容量下平衡语义压缩率和生成性能。

### 方法关键点
- 语义压缩端：动态将文本切分为语义块，用无辅助损失的负反馈机制控制压缩率，结合重构+生成监督学习紧凑的预测型latent表征
- 离散生成端：块因果掩码扩散模型（MDM）解码器在clean/noise/drop三种latent条件下联合训练，推理时用CFG调节语义重构与自主生成的平衡
- 训练机制：token预测梯度通过latent回传更新编码器，实现连续表征与离散生成协同自适应，Flow Matching先验学习用stop-gradient和表征学习解耦
- 推理机制：固定块布局下重编码生成文本，保证latent历史与实际文本上下文对齐，避免累积偏差

### 关键结果
在OLMo 2语料上训练，对比AR、LLaDA、Cola DLM等基线，210B token训练下5下游任务平均性能优于LLaDA；346B token训练的未收敛checkpoint 8任务平均60.10，仅比Llama-3-8B低6.15点（后者预训练token超43倍），且在HellaSwag、StoryCloze两个任务上超过Llama-3-8B。

最值得记住的结论：连续latent层级建模可有效兼容现有自回归、掩码扩散等token空间生成范式，小训练预算下即可实现极具竞争力的生成性能。
