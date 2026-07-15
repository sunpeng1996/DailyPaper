---
title: 'Know Before Fix: QA-Driven Repository Knowledge Acquisition for Software Issue
  Resolution'
title_zh: 先认知再修复：QA驱动的代码库知识获取实现软件问题自动解决
authors:
- Haotian Lin
- Silin Chen
- Xiaodong Gu
- Yuling Shi
- Chengxi Pan
- Jiaqi Ge
- Mengfan Li
- Jianghong Huang
- Mengchieh Chuang
- Beijun Shen
affiliations:
- Shanghai Jiao Tong University
- University of Pittsburgh
- Guangdong Technion–Israel Institute of Technology
arxiv_id: '2607.11111'
url: https://arxiv.org/abs/2607.11111
pdf_url: https://arxiv.org/pdf/2607.11111
published: '2026-07-12'
collected: '2026-07-15'
category: Agent
direction: 编码Agent · 前置知识获取优化
tags:
- Coding-Agent
- QA-Driven
- Knowledge-Acquisition
- Software-Repair
- SWE-bench
one_liner: 提出两阶段QA驱动的代码修复Agent框架ACQUIRE，先获取结构化知识再生成补丁，Pass@1最高提升4.4pp
practical_value: '- 搭建任务型Agent时可采用「先知识获取再执行」的两阶段架构，将复杂任务拆解为多轮定向QA获取上下文，避免直接执行的幻觉与错误，比如电商客服Agent解决用户商品问题时，先基于问题生成结构化疑问查询商品知识库再给出回答

  - 知识获取阶段可采用分类引导的提问模板，覆盖任务所需核心知识维度，避免提问冗余或遗漏关键信息，比如推荐系统用户意图理解模块可预设意图分类引导生成搜索query，提升召回准确率

  - 多并行独立回答Agent的设计可大幅降低知识获取耗时，同时避免不同回答间的上下文干扰，适合业务对latency要求较高的Agent场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM驱动的编码Agent解决代码库问题时，常因对代码库内部知识（跨模块依赖、隐式API契约、数据流逻辑等）不足产生事实错误，现有预探索方法仅基于issue关键词匹配，获取的上下文不精准、覆盖不全，无法填补知识缺口，导致修复成功率低、token成本是成功修复的4倍以上。

### 方法关键点
- 完全解耦知识获取与补丁生成的两阶段架构，模仿资深开发者先理解代码库再修复的行为逻辑
- 知识获取阶段：Questioner基于预设的4类知识维度（机制&行为、设计&使用、定位&结构、生态&标准）生成针对性问题，多个独立Answerer并行探索代码库生成有代码证据支撑的QA对，避免交叉干扰、降低整体耗时
- 修复阶段：Resolver将结构化QA对作为前置上下文，基于可靠知识生成补丁，无需冗余探索

### 关键实验
在SWE-bench Verified 500个真实GitHub issue数据集上测试，对比Mini-SWE-Agent、LocAgent、LingmaAgent等主流基线，在GPT-5-mini上Pass@1提升3.8pp，在DeepSeek-V3.2上提升4.4pp，仅增加少量时间和成本；99.1%的生成QA对符合代码库事实，可减少17.1%的修复步骤。

最值得记住的一句话：任务型Agent的执行准确率瓶颈往往不在于推理能力，而在于对任务特定上下文的认知完备性，先明确知识缺口再定向获取，比直接边执行边探索的效率和准确率更高。
