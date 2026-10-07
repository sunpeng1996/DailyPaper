---
title: Hiding Tool Latency in On-Device Cascaded Voice Agent through Speculative Execution
title_zh: 基于推测执行的端侧级联语音Agent工具延迟隐藏方法
authors:
- Kyudan Jung
- Hyunsin Park
- Yoonhyung Lee
- Jinhwan Park
- Jinhyeok Yang
- KiHyun Nam
- Jaegul Choo
- Jinkyu Lee
affiliations:
- Qualcomm AI Research
- KAIST AI
arxiv_id: '2610.07641'
url: https://arxiv.org/abs/2610.07641
pdf_url: https://arxiv.org/pdf/2610.07641
published: '2026-10-05'
collected: '2026-10-07'
category: Agent
direction: 端侧Agent · 工具调用延迟优化
tags:
- On-device Agent
- Speculative Execution
- Tool Calling
- Latency Optimization
- Speech Assistant
one_liner: 在流式ASR阶段提前预测并执行工具调用，降低端侧语音Agent的响应延迟
practical_value: '- 端侧电商导购/客服Agent场景下，高延迟只读工具（如商品搜索、物流查询、库存查询API）可采用轻量规则预测器在用户语音/文本输入未完成时提前预取，和用户输入时间重叠，降低用户感知延迟

  - 预取结果直接注入LLM prompt的设计可复用：不仅能降延迟，还能给小参数量端侧LLM提供额外任务相关上下文，显著提升工具调用F1，尤其适合端侧3B-7B量级LLM的落地场景

  - 推测执行仅覆盖只读工具的边界设计可直接复用：电商场景下所有查询类工具均可开启推测，写入类（如下单、改地址）工具禁止推测，避免用户输入修正带来的业务风险

  - 端侧前置意图预测的选型参考：轻量规则预测器虽然准确率略低于端侧LLM预测器，但无额外推理开销，更适合低延迟要求的端侧场景，无需为小幅准确率提升引入额外推理延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统级联语音Agent需等待ASR完成、LLM输出工具调用请求后才执行工具，远程工具（如网页搜索、商品查询）的延迟完全暴露在用户等待路径上，端侧交互对延迟敏感度极高，高延迟与高方差会严重损害用户体验，亟需在不降低准确率的前提下隐藏工具调用开销。
### 方法关键点
- 新增轻量规则预测器：流式ASR过程中，收到≥6个词、之后每新增5个词或检测到300ms暂停时触发预测，将当前ASR结果切分为独立子句，匹配12类粗粒度意图生成候选工具调用请求
- 两级缓存利用机制：推测执行的工具结果存入专用缓存，ASR完成后直接将缓存结果注入LLM prompt；若LLM仍发起重复工具调用则优先匹配缓存，无匹配才走正常工具调用路径，最坏情况延迟不超过基线
- 风险控制机制：仅对只读工具执行推测调用，避免用户输入修正（如撤回、意图变更）带来的副作用；规则预测器仅在CPU运行，不占用端侧NPU资源
### 关键实验
在搭载骁龙Elite Gen 5的三星S26 Ultra上部署验证，数据集包含146条覆盖单/多搜索、日历闹钟、无工具需求、硬负例、对抗例的语音请求，对比基线级联系统：
- 中位数TTFA（语音结束到首条TTS输出耗时）从5.79s降至4.60s，p99 TTFA从19.76s降至15.10s，延迟标准差从3.49s降至2.81s，响应更稳定
- 工具调用F1从44.8%提升至60.6%，缓存就绪率达47.7%，仅产生5次无效推测调用
### 核心结论
端侧Agent的延迟优化无需盲目上复杂模型，利用用户输入时间做轻量推测预取，既能显著降低感知延迟，还能为小参数量端侧LLM补充上下文，提升工具调用准确率
