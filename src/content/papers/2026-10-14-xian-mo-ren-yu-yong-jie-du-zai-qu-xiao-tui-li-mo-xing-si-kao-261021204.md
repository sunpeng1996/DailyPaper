---
title: 'Entertain, then Cancel: How Thinking Makes Reasoning Models Read Some and
  Or Literally'
title_zh: 先默认语用解读再取消：推理模型思考时对some/or的字面化偏移
authors:
- Zhizhuo Kou
- Jian Yang
- Pengfei Hao
- Junyu Luo
- Jingshu Peng
- Sirui Han
- Yike Guo
affiliations:
- The Hong Kong University of Science and Technology
- The Hong Kong University of Science and Technology (Guangzhou)
- Peking University
arxiv_id: '2610.21204'
url: https://arxiv.org/abs/2610.21204
pdf_url: https://arxiv.org/pdf/2610.21204
published: '2026-10-14'
collected: '2026-10-22'
category: Reasoning
direction: 大模型推理 · 语用隐含解读
tags:
- Reasoning Model
- Scalar Implicature
- Pragmatic Understanding
- Chain of Thought
- Trace Extraction
one_liner: 揭示推理模型思考时会取消some/or的语用隐含，提出基于trace前缀的修复方案
practical_value: '- 搭建电商客服Agent时，若使用带思考模式的推理模型处理用户口语化查询，可提取前128个思考token的结果还原some/or类表述的真实语用意图，避免最终推理结果过度字面化误解用户需求

  - 做搜索query理解时，针对用户模糊查询的隐含意图识别，可参考trace截断方法，在CoT推理早期阶段提取意图，平衡逻辑推理准确性和语用贴合度

  - 训练行业定制推理模型时，可在SFT/DPO阶段针对性保留标量隐含的语用解读规则，避免推理能力提升后过度字面化，适配日常对话、导购类场景需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前推理模型的思考开关/时长可由用户自定义，现有研究仅关注思考对数学、代码任务的效果提升，未明确思考过程对日常对话中语用隐含（如some表“并非全部”、or表“二选一”）的影响，单一准确率指标也无法区分模型是理解用户意图还是仅做字面推理，亟需明确思考对语用解读的作用机制。

### 方法关键点
- 固定模型权重，仅调整思考开关/思考token预算，对比不同思考程度下模型的语用解读差异
- 提出trace前缀诊断法：逐段截断推理trace，在每个截断点强制输出答案，定位解读变化的时间节点
- 覆盖40个开源推理模型、7个闭源模型，测试集包含逻辑词（some/or）、词汇等级、预设、间接回答四类语用场景

### 关键结果数字
30/40开源模型、GPT-5开启思考模式后，some/or的语用解读占比下降20~50pp，仅语境驱动的间接回答、预设识别准确率提升5~17pp；67.4%的Qwen3-8B推理trace呈现“先语用后字面”轨迹：前128token时some的语用解读占比达52%，完整推理后降至1.1%；基于前128token提取答案的修复方案，可将some/or的语用解读准确率从1.2%提升至20.5%，且不损失字面推理准确性。

### 核心结论
推理模型的长思考会让逻辑词解读过度字面化，实际业务中不能只看最终推理结果，早期trace里往往保留了更符合用户真实意图的解读
