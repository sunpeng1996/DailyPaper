---
title: 'Influence Score and Transformers interpretability: Measure of the Effective
  Impact of Attention Heads at inference time'
title_zh: Transformer可解释性影响分数：推理阶段注意力头有效贡献度量
authors:
- Lisa Bouger
- Yannick Teglia
- Philippe Loubet Moundi
affiliations:
- Thales CDI, France
- Inria Paris, France
- Sorbonne Université, France
arxiv_id: '2609.05074'
url: https://arxiv.org/abs/2609.05074
pdf_url: https://arxiv.org/pdf/2609.05074
published: '2026-09-04'
collected: '2026-09-07'
category: LLM
direction: LLM可解释性 · 注意力头贡献量化
tags:
- Transformer Interpretability
- Attention Head
- Prompt Injection Detection
- Residual Stream
- LLM Security
one_liner: 提出结合logits方向影响与残差流结构贡献的注意力头影响分数，实现Transformer分类器多粒度可解释分析
practical_value: '- 可复用influence score计算逻辑，分析业务LLM（如生成式推荐prompt理解模块、Agent安全模块）的注意力头贡献，定位低效/错误头做剪枝，降低推理延迟

  - 可借鉴残差流+logits双维度贡献评估思路，用于大模型排序模块的bad case归因，快速定位预测偏差的网络层来源

  - 该多粒度（头/层/网络）分析框架可直接迁移到prompt注入检测模块优化，提升电商Agent、导购LLM的安全防御稳定性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM上游部署的prompt注入检测等Transformer分类器黑盒性强，现有可解释方法要么电路级细粒度分析计算成本极高，要么全局输出导向分析粒度太粗，无法精准定位推理阶段注意力头的实际贡献，难以支撑bad case归因与模型可靠性优化。
### 方法关键点
提出influence score，融合双维度贡献计算：1）注意力头输出对最终logits的方向影响；2）注意力头在残差流中的结构贡献，支持头、层、全网络三个粒度的可解释分析。
### 关键结果
在prompt注入检测专用DeBERTa模型上验证，可有效区分正确预测与错误预测的决策行为差异，实现了细粒度电路分析与全局输出方法的效果折中，为Transformer分类器决策机制研究提供了系统化路径。
