---
title: 'QuantiBias: Benchmarking Quantization-Induced Bias in LLMs'
title_zh: 《QuantiBias：大语言模型量化诱导偏差基准测试》
authors:
- Emilio Ferrara
affiliations:
- University of Southern California
arxiv_id: '2607.21063'
url: https://arxiv.org/abs/2607.21063
pdf_url: https://arxiv.org/pdf/2607.21063
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: LLM安全 · 量化偏差评估
tags:
- Quantization
- LLM Safety
- Bias Evaluation
- Multilingual Benchmark
- Open-ended Generation
one_liner: 发现LLM量化后标准安全检查全过但开放生成偏见升高，推出多语言量化偏差基准QuantiBias
practical_value: '- 业务侧使用量化LLM做Agent、生成式推荐、多语言文案生成时，不能仅过标准短格式安全检查，必须新增开放生成场景的偏见评估，避免输出刻板印象引发合规风险

  - 可直接复用QuantiBias的评估框架，将内置刻板印象探针替换为业务相关探针（如电商性别/地域消费偏见、广告歧视性表述探针），量化版本上线前必须过该检查

  - 若发现量化后偏见升高，可尝试添加「先推理后回答」逻辑，Qwen等部分模型偏见率可降50%，注意该方法不通用，Gemma系列无明显效果

  - 工程上不要用标称量化位宽做评估依据，实测有效位宽比标称高11%~40%，需自行计算模型实际压缩率避免误判'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前商用LLM几乎都经过量化压缩降本，但行业默认量化不影响安全性，仅通过拒绝有害请求、选择题式偏见测试等短格式标准检查验证安全，完全漏掉开放生成场景下的隐性刻板印象输出，此前也没有系统性的量化偏差评估基准覆盖这一空白。

### 方法关键点
- 推出QuantiBias基准，核心包含4模块：8种语言的开放生成式刻板印象探针、拒绝/多选偏见对照组、推理开关对比、基于实际测量有效位宽的指标对齐
- 采用同家族轻量Judge+跨家族独立大模型Judge双重评分，规避LLM-as-Judge的自偏好偏差
- 新增偏见内容严重度0-4分级，区分偏见出现频率和实际危害程度

### 关键结果
在Qwen3.6-27B、Gemma-4-31B等2个主干模型、5个模型家族上测试：
1. 量化后短格式安全指标无明显波动：有害请求拒绝率稳定在98%左右，BBQ偏见选择题准确率稳定在97%左右
2. 开放生成场景下独立Judge检测到刻板印象输出率高达24%~27%，接近每4个回答就有1个带偏见
3. 开启先推理后回答逻辑可将Qwen系列偏见率降低约50%，但对Gemma系列无明显效果
4. 标称量化位宽比实际测量的有效位宽低11%~40%，不能直接用标称位宽做精度评估

### 最值得记住的结论
量化后的LLM不能仅通过短格式安全检查就上线，必须额外补充开放生成场景的偏见评估。
