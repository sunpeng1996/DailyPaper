---
title: What Gradients Add to Text Leakage in Split Language Models, Counted per Token
  and per Document
title_zh: 拆分大语言模型中梯度对文本泄露的贡献：逐token与逐文档量化
authors:
- Georgios Politis
- Evangelos Pappas
affiliations:
- Setloop.io
arxiv_id: '2610.04128'
url: https://arxiv.org/abs/2610.04128
pdf_url: https://arxiv.org/pdf/2610.04128
published: '2026-10-01'
collected: '2026-10-06'
category: LLM
direction: 大语言模型 · 拆分训练隐私安全
tags:
- Split-LLM
- Split-Learning
- Privacy-Leakage
- Gradient-Leakage
- Text-Recovery
one_liner: 量化拆分LLM训练中梯度对文本泄露的增量贡献，提出双维度泄露评估标准
practical_value: '- 业务侧若采用拆分LLM训练处理用户敏感文本（如搜索query、电商评论），不可默认仅传激活无泄露，梯度回传会显著提升文本恢复概率，敏感场景需额外增加隐私防护手段

  - 评估隐私防御方案效果需同时采用逐token恢复率、逐文档全匹配率双指标，避免被单指标误导，例如secret mixup几乎阻断整文档恢复，但仍有83~91%的token可被恢复

  - 拆分LLM部署时，切分层位置选择需同时权衡模型效果和泄露风险，即使切分的层数量固定，不同切分点的泄露程度存在明显差异'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
拆分LLM训练方案通过本地运行前几层、仅上传激活向量的方式，被认为可避免用户原始文本泄露，但梯度回传带来的额外泄露风险未被量化，单一的评估指标也容易高估防御效果。
### 方法关键点
1. 基于公开的客户端层权重构造攻击方案，分别测试仅观察激活、同时观察激活+梯度两种场景下的文本恢复能力
2. 采用逐token恢复准确率、逐文档全匹配准确率双维度衡量泄露程度
3. 测试不同切分层位置、secret mixup防御方案的实际表现
### 关键结果数字
GPT-2场景下，仅用激活可恢复94.20%的token，增加梯度观测后提升至97.38%；逐文档全匹配准确率从13.71%跃升至37.77%；secret mixup可将整文档恢复率压到极低，但单token恢复率仍达83~91%；切分层位置会同时影响模型质量和泄露程度。
