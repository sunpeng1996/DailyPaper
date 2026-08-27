---
title: Unfolding Scientific Papers into Multi-Turn Generation Trajectories for Continued
  Pre-Training
title_zh: 将学术论文拆解为多轮生成轨迹用于大模型继续预训练
authors:
- Qiankai Xu
- Qiguang Chen
- Zixin Su
- Wenhao Huang
- Yue Gao
- Jiaheng Liu
- Ge Zhang
affiliations:
- ByteDance Seed
- Nanjing University
- Evolvent AI
arxiv_id: '2608.25826'
url: https://arxiv.org/abs/2608.25826
pdf_url: https://arxiv.org/pdf/2608.25826
published: '2026-08-26'
collected: '2026-08-27'
category: Training
direction: 大模型训练 · 半合成轨迹数据构造
tags:
- Synthetic Data
- Continued Pre-Training
- SFT
- Long-Context LLM
- Benchmark
one_liner: 逆向还原学术论文写作全流程轨迹，产出预训练语料、SFT数据集与学术写作基准
practical_value: '- 复用「固定真实内容反向推导前置思考/意图」范式构造文案训练数据：固定优质商品详情页/广告文案，反向生成用户需求、内容策划思路，提升LLM生成文案的合理性，减少幻觉

  - 小模型生成半合成训练数据的结论可落地：不需要大模型生成训练数据，4B小模型产出的轨迹数据效果优于27B，大幅降低领域专用预训练语料的构造成本

  - 复用多输出物统一数据pipeline：同一套业务原始数据（商品、评价、交易数据）可同时产出预训练语料、SFT数据集、业务效果评测基准，降低数据生产冗余

  - 长上下文训练样本构造思路可复用：在原始短文本之间插入合理过渡思考内容，将短文本拼接为长文档训练样本，低成本提升模型长上下文理解能力，适配电商长文本处理场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于短文本的半合成训练数据仅恢复局部思考，忽略长文档整体结构，无法为模型提供完整的生成过程训练信号；高质量人类文本接近枯竭，学术论文结构清晰规范，是天然的长文档级半合成数据来源。

### 方法关键点
- 统一逆向构造范式：固定真实文本作为最终输出，反向推导前置生成过程，同一套arXiv论文数据可产出三类产物：继续预训练（CPT）轨迹语料、SFT数据集、PAW-Bench学术写作基准
- CPT轨迹构造：将1.8M篇arXiv论文拆解为「写作请求→全局大纲→分节预写作思考→对应章节原文→摘要生成思考→摘要原文」的多轮轨迹，原始论文内容100%保留，仅思考部分由LLM生成，语料规模从30B tokens扩张到60B tokens，平均长度从11K提升到29K
- SFT数据集构造：固定论文单段内容作为答案，反向生成对应任务prompt和前置思考，产出20万条覆盖29类学术读写任务的SFT样本
- PAW-Bench构造：基于时间窗切分的未训练论文，生成带评分规则和可自动化校验checklist的2940条学术写作评测任务

### 关键实验
基于Qwen2.5-7B做对照实验，对比纯FineWeb-Edu、原始论文文本两个baseline：轨迹CPT+通用SFT后，学术写作指标平均提升4.7%，PAW-Bench得分提升3.5~4.0；通用推理能力无损失，MMLU等推理指标与基线持平甚至略优；32K-64K长度的LongBench v2得分最高提升6.0；4B小模型生成的轨迹数据效果优于9B/27B大模型的产出，成本更低。

### 核心结论
半合成训练数据的价值核心是结构和信号密度，而非生成模型的大小，更难拟合的低生成质量数据反而能带来更好的下游效果。
