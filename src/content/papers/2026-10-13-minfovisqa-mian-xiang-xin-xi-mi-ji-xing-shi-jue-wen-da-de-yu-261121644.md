---
title: 'MInfoVisQA: A Multilingual Benchmark for Information-Rich Visual Question
  Answering'
title_zh: MInfoVisQA：面向信息密集型视觉问答的多语言评测基准
authors:
- Changjiang Jiang
- Jiang Zhou
- Xinbin Yuan
- Fan Zhang
- Tao Feng
- Zhuohan Xie
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Georgia Institute of Technology
- The University of Tokyo
- University of Illinois at Urbana-Champaign
arxiv_id: '2611.21644'
url: https://arxiv.org/abs/2611.21644
pdf_url: https://arxiv.org/pdf/2611.21644
published: '2026-10-13'
collected: '2026-11-19'
category: Multimodal
direction: 多模态大模型 · 多语言VQA评测
tags:
- MLLM
- VQA
- Multilingual
- Benchmark
- Multimodal
one_liner: 推出覆盖24种语言的信息密集型VQA基准MInfoVisQA，完成25款MLLM跨语言性能评测
practical_value: '- 做跨境电商多语言商品图文理解、经营报表自动问答Agent时，不能仅依赖平均准确率评估MLLM性能，需补充跨语言图文对齐鲁棒性测试

  - 开发多语言信息可视化（如商家数据看板、用户消费分析图表）自动问答功能时，可复用本研究「解耦数值结构与文本、批量生成多语言对齐图表+QA对」的数据集构建方法

  - 跨境场景多模态MLLM选型时，不能仅参考英文VQA指标，需额外测试非英语图文对的匹配准确率，避免跨语言性能落差过大'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前MLLM在视觉语言任务表现优异，但面向信息密集型可视化内容（InfoVis，如图表、经营报表）的跨语言理解一致性未被量化，缺少对应评测基准。
### 方法关键点
1. 构建MInfoVisQA基准，覆盖24种语言，从128个种子实例生成8960组QA配置；
2. 通过解耦数值结构数据与文本、程序化同步翻译标签的方式，生成种子匹配、语言平行的可视化内容与QA对；
3. 设置两类评测场景：Language-Aligned QA（LQA，图文语言一致）、Cross-Language QA（XQA，QA语言固定、可视化内容语言变化），共评测25款MLLM。
### 关键结果数字
- 平均准确率掩盖显著鲁棒性差距：两款LQA平均准确率同为80.4%的模型，跨语言性能落差分别达7.8、20.3个百分点；
- 固定QA为英语时，所有25款模型在非英语可视化内容上的得分均低于英语可视化内容。
