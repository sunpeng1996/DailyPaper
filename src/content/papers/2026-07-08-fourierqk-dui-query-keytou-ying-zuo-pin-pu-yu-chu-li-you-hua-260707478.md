---
title: 'FourierQK: Spectral Preprocessing of Query-Key Projections Improves Transformer
  Attention'
title_zh: FourierQK：对Query-Key投影做频谱预处理优化Transformer注意力
authors:
- Athanasios Zeris
arxiv_id: '2607.07478'
url: https://arxiv.org/abs/2607.07478
pdf_url: https://arxiv.org/pdf/2607.07478
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: Transformer注意力优化 · 频谱预处理
tags:
- Transformer
- Attention Optimization
- FFT
- Spectral Preprocessing
- QK Projection
- Language Modeling
one_liner: 对Transformer的Q/K投影做FFT频谱预处理，字符级语言建模任务验证损失最高降79%
practical_value: '- 生成式推荐、Query理解类Transformer模型可直接复用该Q/K频谱预处理方案，无需改动注意力核心结构，工程改造成本极低即可获得效果增益

  - 长序列用户行为建模、会话推荐场景可参考多尺度频率设计，分别对应长周期偏好、会话、单次交互等不同粒度的行为特征融合

  - 离线预训练优化时可优先测试单学习频率的轻量方案，本文验证其效果稳定、可复现性强，适合快速上线验证'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
标准Transformer点积注意力仅建模两两token交互，缺乏全局序列的多尺度频率特征融合，在细粒度序列建模任务上损失较高；已有FNet等方案完全替换注意力结构，丢失了原注意力的可解释性和结构优势。
### 方法关键点
仅对Transformer的Q、K学习投影做FFT频谱预处理，保留完整注意力打分结构；支持固定随机滤波、单学习频率、多学习频率三种实现，多频率可覆盖从词到段落的多尺度序列特征。
### 关键结果
在TinyShakespeare字符级语言建模任务上：固定随机滤波验证损失1.031，较基准提升0.443；单学习频率验证损失0.608，较基准提升0.867，三随机种子平均损失0.236，标准差0.019，可复现性强；4个多尺度学习频率方案验证损失0.309，较基准提升1.166，损失降低79%，收敛到49/27/10/6 tokens/周期的近几何多尺度分布，分别对应段落、子段落、短语、词粒度。
