---
title: Synthetic Pre-pretraining Survives Scale, but Not as a Grammatical Prior
title_zh: 合成预预训练可在大尺度下生效，但并非通过语法先验实现
authors:
- Atsuki Yamaguchi
- Tatsuro Inaba
- Joel Niklaus
- Michal Štefánik
- Aline Villavicencio
- Nikolaos Aletras
affiliations:
- University of Sheffield
- Mohamed bin Zayed University of Artificial Intelligence
- Hugging Face
- National Institute of Informatics
- University of Exeter
arxiv_id: '2609.39827'
url: https://arxiv.org/abs/2609.39827
pdf_url: https://arxiv.org/pdf/2609.39827
published: '2026-09-29'
collected: '2026-10-01'
category: Training
direction: LLM预训练优化 · 合成预预训练
tags:
- Pre-pretraining
- Synthetic Data
- LLM Training
- Long-range Retrieval
- Scaling
one_liner: 系统性验证合成预预训练在7B参数、100B token下仍生效，增益来自长程检索而非语法先验
practical_value: '- 训练3B/7B级垂直场景小/中基座时，可加500步k-Shuffle Dyck/NCA合成预预训练，仅用1%计算量就能节省至少21B预训练token，显著降低训练成本

  - 优化长上下文RAG/Agent基座时，优先选择带长程检索目标的合成预训练任务，比语法结构类任务的落地增益更稳定

  - 电商营销文案/商品描述生成垂直基座训练中，只要预训练数据包含通用网页文本，加合成预预训练的增益不受代码/数学数据占比影响，可直接复用开源实现'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
过往合成预预训练（PPT）仅在≤1B参数、≤2B训练token的小尺度下被验证有效，且增益被归因于学习到的语法先验；但工业级大模型训练普遍采用≥3B参数、≥10B训练token、多领域混合数据的设定，PPT在真实大尺度训练下是否仍生效、增益来源是否正确尚属空白，直接影响该技术的落地可行性。
### 方法关键点
- 覆盖5类PPT任务：2种形式语法任务（k-Shuffle Dyck、MP-Struct Core）、2种无语法结构化任务（集合去重、神经细胞自动机NCA）、1个域内文本对照任务
- 测试4种工业界常用预训练数据混合方案：纯网页文本C4、网页主导Marin、均衡代码数学的SmolLM3、STEM加权OLMo3
- 验证4种主流参数尺度（500M/1B/3B/7B），预训练token最高达100B，覆盖小/中基座全量级
### 关键结果
对比无PPT的PT-Only基线，3B参数下PPT可节省至少21B预训练token，仅需额外1%左右的预训练计算量；9/12参数-数据组合下下游任务平均得分提升1.6分，增益在7B参数、100B训练token下仍为正；语法接受度BLiMP无稳定提升，12组实验中仅1组有稳定增益，而长程检索任务NLL在全部12组实验中均下降，验证增益核心来自长程检索能力提升；仅当预训练数据完全不含网页文本时PPT增益消失，代码/数学占比提升13倍也不会降低增益。
### 核心结论
合成预预训练是低投入高回报的预训练优化手段，任务设计应优先瞄准长程检索能力，而非模仿自然语言语法结构
