---
title: Can MLLMs Decode the Creative Leap? Introducing C4 for Cross-Concept Understanding
title_zh: 多模态大模型跨概念创造力评估：C4认知启发基准框架
authors:
- Ming Wang
- Yuqing Zhang
- Tingna Xie
- Xiangju Li
- Xiaocui Yang
- Daling Wang
- Shi Feng
- Yifei Zhang
affiliations:
- Northeastern University
- Singapore Management University
- Shandong University of Science and Technology
- KinaMind
arxiv_id: '2608.06501'
url: https://arxiv.org/abs/2608.06501
pdf_url: https://arxiv.org/pdf/2608.06501
published: '2026-08-05'
collected: '2026-08-10'
category: Eval
direction: 多模态大模型 · 创造力评估
tags:
- MLLM
- Cross-Concept Understanding
- Creativity Evaluation
- Benchmark Dataset
- Evaluation Framework
one_liner: 提出基于中文成语的认知启发式C4跨概念创造力评估框架及配套评测集
practical_value: '- 跨概念关联映射方法可复用至电商创意素材生成场景，支撑成语梗、谐音梗类商品宣传文案/海报的创意生成与合规校验

  - 带桥接路径难度标注的基准构建方法可迁移到垂类Agent能力评测，比如电商营销Agent、内容创意Agent的创造力分层评测

  - 垂类MLLM推理时可参考论文结论，增加候选输出范围约束，能大幅提升创意类任务的输出准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
MLLM创造力在设计、营销、人机协作等场景价值突出，但相比精度导向任务缺乏明确评估目标与奖励信号，难以量化评测；跨概念理解是接收式创造力的核心认知能力，现有评估体系未覆盖该维度。
### 方法关键点
提出认知启发的C4跨概念创造力评估框架，以中文成语为载体，构建人工标注第三方审核的跨概念网络：编码阶段将目标槽沿桥接路径映射到可可视化替代概念，可批量生成标注了桥接数量/深度难度、有明确标准答案的评测样本；基于框架构建C4-Eval评测集，包含184个合成样本、37个人工创作样本，覆盖5种任务设置共884个答案恢复案例。
### 关键结果
10款MLLM评测中，最强闭源模型准确率仅为50.7%、48.0%，开源模型准确率远低于闭源；增加候选约束可大幅提升准确率，桥接提示、要求解释仅带来小幅提升，当前MLLM跨概念创造力存在明显短板。
