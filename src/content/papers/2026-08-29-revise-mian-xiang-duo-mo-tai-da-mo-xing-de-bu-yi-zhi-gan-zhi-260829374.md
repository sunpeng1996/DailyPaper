---
title: 'Think, Look, and Revise: Inconsistency-Aware Visual Self-Correction in MLLMs'
title_zh: ReVISE：面向多模态大模型的不一致感知视觉自校正框架
authors:
- Yu Cheng
- Arushi Goel
- Hakan Bilen
affiliations:
- University of Edinburgh
- NVIDIA Research
arxiv_id: '2608.29374'
url: https://arxiv.org/abs/2608.29374
pdf_url: https://arxiv.org/pdf/2608.29374
published: '2026-08-29'
collected: '2026-09-01'
category: Multimodal
direction: 多模态大模型 · 工具推理自校正
tags:
- MLLM
- Tool-Augmented Reasoning
- Self-Correction
- GRPO
- Visual Grounding
one_liner: 为工具增强多模态大模型设计带验证自校正的闭环框架 结合专项SFT与GRPO奖励提升感知任务表现
practical_value: '- 搭建电商商品多模态理解Agent时，可复用工具输出校验逻辑，对低置信度的目标检测、属性识别结果触发重查或区域放大，降低商品定位、空间关系判断的错误率

  - 训练工具调用Agent时，可参考本文5类推理轨迹的SFT构造方法，搭配GRPO的自校正、grounding专项奖励，大幅提升工具调用的鲁棒性，减少盲信工具的错误

  - 做多模态商品导购、实景逛街推荐时，可复用grounding奖励设计，要求模型输出对应商品的bounding box，用IoU约束强化空间定位能力，降低导购回答的幻觉'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有工具增强MLLM采用开环执行逻辑，盲目信任工具输出，工具识别错误会直接传导到最终结果；同时训练阶段缺乏对自校正行为的监督，模型过度依赖工具反而弱化了自身视觉推理能力，在感知密集的空间判断、计数、定位等任务上鲁棒性极差。

### 方法关键点
- 构造覆盖5类场景的SFT数据集：包含工具结果校验通过、工具结果错误重试、工具失效fallback到自有能力、无工具校验正确、无工具校验纠错5种多轮推理轨迹，监督模型的不一致检测与自校正行为
- 基于GRPO设计4项组合奖励：除基础的答案准确率、格式合规奖励外，新增自校正奖励（鼓励触发re-examine逻辑并得到正确结果）、grounding奖励（结合IoU与IoU提升幅度，强化模型空间定位能力）
- 推理时新增闭环校验逻辑：工具返回结果后先与查询、模型自身感知做一致性校验，不一致则重新调用适配工具（如调整裁剪区域、放大倍数）或切换到自有能力推理

### 关键实验
基于Qwen2.5-VL 3B/7B backbone，在CountBench、CVBench、BLINK-HARD等感知密集基准上测试，对比ReVPT、CodeDance等SOTA工具增强MLLM：ReVISE-7B在CountBench上达到92.89%，超此前SOTA 1.69个百分点；CVBench上达到79.12%，超此前SOTA 5.01个百分点；BLINK-HARD上达到63.89%，超此前SOTA 3.41个百分点，工具调用错误恢复率最高超60%。

**最值得记住的一句话：** 工具增强大模型的核心不是学会调用工具，而是学会判断工具结果的可靠性，具备动态纠错与fallback能力
