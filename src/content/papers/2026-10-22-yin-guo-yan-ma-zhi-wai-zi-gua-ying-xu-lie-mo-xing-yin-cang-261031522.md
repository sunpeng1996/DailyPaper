---
title: 'Beyond Causal Masks: Auditing and Localizing Hidden Future-Token Leakage in
  Adaptive Sequence Models'
title_zh: 因果掩码之外：自适应序列模型隐藏未来token泄漏的审计与定位
authors:
- Huiting Liu
- Jinsong Wu
affiliations:
- Guilin University of Electronic Technology
- University of Chile
arxiv_id: '2610.31522'
url: https://arxiv.org/abs/2610.31522
pdf_url: https://arxiv.org/pdf/2610.31522
published: '2026-10-22'
collected: '2026-10-23'
category: Eval
direction: 自回归模型 · 因果泄漏检测
tags:
- Autoregressive Model
- Causal Mask
- Leakage Detection
- Sequence Modeling
- Fault Localization
one_liner: 提出前缀不变性审计框架与LeakScore指标，可检测定位序列模型隐藏未来token泄漏，避免虚假架构增益
practical_value: '- 上线LLM-based生成式推荐、Agent推理服务前，除常规指标外必须增加前缀不变性审计，避免仅依赖teacher-forcing验证loss导致上线后生成质量大幅退化

  - 自研带MoE路由、用户序列全局聚合、跨时间归一化的推荐/广告序列模型时，可直接复用LeakScore和FirstLeakLayer方法排查非因果路径，无需自研检测工具

  - 训练电商文案生成、用户行为序列预测等自回归模型时，所有涉及全局池化、动态路由的逻辑必须严格限制仅访问当前位置及之前的前缀信息，从根源避免隐性未来泄漏'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
自回归模型仅依靠因果注意力掩码无法避免全局池化、动态路由、跨时间归一化等辅助操作引入的隐藏未来token泄漏，会导致teacher-forcing模式下验证loss虚低，给架构优化带来错误引导，上线后自由生成效果会大幅退化，而业界此前缺乏易用的非侵入式泄漏检测与定位工具。

### 方法关键点
- 基于前缀不变性原则设计审计流程：构造共享前缀、不同后缀的序列对，对比模型在共享前缀的输出差异，超过预设数值阈值即判定存在泄漏
- 提出LeakScore量化泄漏程度，即前缀输出的最大∞范数偏差，配套top-1 token翻转率、受影响token占比、JS散度等辅助指标做细粒度诊断
- 设计FirstLeakLayer逐层定位机制，通过对比每层隐状态的前缀输出差异，精准定位泄漏首次出现的网络层级，指导代码排查
- 覆盖多精度（float32/fp16/bf16）、KV cache一致性校验，适配实际工业落地场景

### 关键结果
实验基于OpenWebText数据集，覆盖GPT-2、Qwen2.5、Mamba等公开模型及自研CDR-AttnRes decoder：异常24层CDR模型验证loss从基线的3.5958降至1.4259，但LeakScore高达34.22，自由生成的参考perplexity是基线的42倍；2种因果修复后的模型LeakScore归零，验证loss回到3.67左右，生成perplexity回落至基线水平；6类合成非因果模块的检测准确率达100%，故障注入检测灵敏度可捕捉α=0.01的微小泄漏。

因果注意力掩码不能替代全链路因果校验，低teacher-forcing损失必须结合自由生成评估和因果审计，才能判定为真实的架构性能增益。
