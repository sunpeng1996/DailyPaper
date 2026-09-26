---
title: 'To Trust or Not to Trust: Retrieval-Augmented Fact Checking in Speech'
title_zh: 语音场景下检索增强事实核查的可信度研究
authors:
- Debajyoti Mazumder
- Mamta
- Abhirama Subramanyam Penamakuri
affiliations:
- IISER Bhopal
- King’s College London
- MBZUAI
arxiv_id: '2609.30227'
url: https://arxiv.org/abs/2609.30227
pdf_url: https://arxiv.org/pdf/2609.30227
published: '2026-09-24'
collected: '2026-09-26'
category: RAG
direction: 检索增强 · 多模态事实核查
tags:
- RAG
- Fact Checking
- LALM
- Multimodal
- Benchmark
one_liner: 发布VeriSpeak语音事实核查基准，验证检索结合显式推理可大幅提升LALM核查准确率
practical_value: '- 直播/短视频语音内容合规、语音助手问答等语音交互场景，可复用「RAG+CoT显式推理」架构解决跨模态事实校验问题，规避纯检索的证据-输入混淆问题

  - 跨模态（语音输入+文本知识库）任务优化可优先对基座做推理思维微调，比仅新增RAG模块的效果增益更显著

  - 若需搭建语音类内容事实校验的业务评估流程，可直接复用开源VeriSpeak数据集做预验证，降低自有标注成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前播客、社交视频、演讲等语音类内容中的错误信息传播问题突出，现有事实核查能力多针对文本场景，缺乏语音场景的专用评估基准与成熟落地方案。
### 方法关键点
1. 开源VeriSpeak基准数据集，包含3879条覆盖时间、地理、关系类事实的语音声明，真假标签均衡；
2. 对比6类验证pipeline，测试LALM的文本到语音事实校验能力迁移效果，验证检索增强结合显式推理的性能增益。
### 关键结果
- 存在显著文本-语音模态gap：文本事实校验表现优异的LALM在同内容语音输入上准确率大幅下降；
- 纯RAG增益有限，模型易混淆检索证据与语音声明；
- RAG结合CoT显式推理的思维微调LALM准确率可达86.1%，为当前最优方案。
