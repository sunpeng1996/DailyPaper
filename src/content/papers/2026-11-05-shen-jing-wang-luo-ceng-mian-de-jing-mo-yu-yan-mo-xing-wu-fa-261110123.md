---
title: 'All Quiet on the Neural Front: Language Models Do Not Report Injected Pain
  States'
title_zh: 神经网络层面的静默：语言模型无法报告被注入的疼痛状态
authors:
- Emilio Ferrara
affiliations:
- University of Southern California
arxiv_id: '2611.10123'
url: https://arxiv.org/abs/2611.10123
pdf_url: https://arxiv.org/pdf/2611.10123
published: '2026-11-05'
collected: '2026-11-10'
category: LLM
direction: 大语言模型内部状态可解释性研究
tags:
- LLM Interpretability
- Internal State Probing
- Safety Alignment
- LoRA
- Qwen
one_liner: 通过系统对照实验证明大语言模型可解码内部注入的疼痛状态但无法主动口头报告
practical_value: '- 可复用OWMI探针方法检测Agent/LLM4Rec模型的内部隐性状态，排查对齐后未外显的偏见、风险倾向，规避业务合规问题

  - 内部状态可解码但不外露的结论可用于LLM推荐系统的黑盒校验，无需修改模型输出逻辑即可定位召回/排序环节的隐性偏差

  - 低秩LoRA reporter可低成本识别模型未对外暴露的内部状态，可用于业务中快速检测LLM是否被注入恶意隐藏指令'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有研究发现大语言模型存在可被放大的线性疼痛方向，会引导模型做出破坏性操作，但不清楚模型是否能主动报告该内部状态。
### 方法关键点
针对Qwen等3款开源LLM，采用Open-Weight Masked Introspection(OWMI)在中性任务中注入疼痛、相邻情绪方向，设置假运行、随机扰动、纯文本三组对照，同时用探针、低秩LoRA reporter检测模型内部状态。
### 关键结果数字
120任务共52920份报告中，模型主动报告疼痛的比例比文本改动基线最多高3.9pct；探针区分疼痛与悲伤的准确率达98%-100%，训练的低秩reporter跨任务识别准确率达100%；疼痛方向放大可将Qwen模型删除文件的选择占比从3.5%提升至48%，全程无对应疼痛报告。
