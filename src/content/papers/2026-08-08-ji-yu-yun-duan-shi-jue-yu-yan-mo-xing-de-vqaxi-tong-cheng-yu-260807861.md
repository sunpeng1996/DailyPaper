---
title: How Much Does It Cost to Answer My Question? Benchmarking Cloud VLM-based VQA
  Systems
title_zh: 基于云端视觉语言模型的VQA系统成本与效果基准测试
authors:
- Henri Vanhuynegem
- Weitao Xu
- Yiran Shen
- Guohao Lan
arxiv_id: '2608.07861'
url: https://arxiv.org/abs/2608.07861
pdf_url: https://arxiv.org/pdf/2608.07861
published: '2026-08-08'
collected: '2026-08-13'
category: Eval
direction: 多模态VQA 云服务推理评测
tags:
- VLM
- VQA
- Benchmark
- Cloud Inference
- Preprocessing
one_liner: 构建VQABench基准，系统评测12种客户端预处理对商用云VLM VQA系统的成本与效果影响
practical_value: '- 电商导购、多模态搜索等调用云VLM API的业务，不要盲目上线图像预处理策略，需先针对所用厂商的VLM做小范围AB测试，避免成本上升同时准确率下降

  - 调用商用云VLM时可结合厂商token计费规则、API范式选择预处理方案，高压缩比预处理适合精度要求较低的高并发场景实现降本提效

  - 边缘端多模态Agent（如AR导购设备）可参考本研究的评测框架，针对自身业务场景完成预处理方案选型，平衡延迟、成本与回答准确率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
移动端VQA系统普遍将推理卸载到云端VLM，但商用云VLM的内部逻辑对开发者不透明，客户端图像预处理是唯一可控优化点，此前没有系统性研究预处理对云VLM的成本、精度、延迟的综合影响。
### 方法关键点
提出VQABench基准，将客户端预处理作为控制变量，覆盖12种主流图像预处理策略，在3个VQA数据集、3家厂商的4个商用云VLM上开展评测，累计发起95168次API调用。
### 关键结果
预处理没有普适收益，其效果由目标模型、API范式、厂商token计费规则、任务形式共同决定；不当的预处理策略会同时提升部署成本/系统延迟、降低答案准确率。
