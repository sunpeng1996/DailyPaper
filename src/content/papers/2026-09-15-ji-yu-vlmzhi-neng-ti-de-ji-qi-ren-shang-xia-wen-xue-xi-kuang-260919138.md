---
title: In-Context Robot Learning with VLM Agents
title_zh: 基于VLM智能体的机器人上下文学习框架GPT-Policy
authors:
- Dongzhou Cheng
- Taoran Yi
- Ye Fang
- Xingwu Zhang
- Fan Feng
- Yixuan Li
- Gengxiong Zhuang
- Rongze Wang
- Shuai Yang
- Wei Song
affiliations:
- Morphi Robot
- Shanghai Innovation Institute
- Huazhong University of Science and Technology
- Fudan University
- Hunan University
arxiv_id: '2609.19138'
url: https://arxiv.org/abs/2609.19138
pdf_url: https://arxiv.org/pdf/2609.19138
published: '2026-09-15'
collected: '2026-09-17'
category: Agent
direction: 具身Agent · VLM上下文学习
tags:
- VLM
- In-Context Learning
- Embodied Agent
- Robot Learning
- Zero-shot Adaptation
one_liner: 提出无梯度更新的VLM驱动机器人上下文学习框架GPT-Policy，可基于演示、反馈生成可验证的实体机器人动作
practical_value: '- 可复用「上下文编译器+大模型推理+约束控制器」三段式Agent架构：上下文编译器过滤任务无关输入降低噪声，约束控制器兜底大模型输出合法性，适配电商导购Agent、个性化推荐Agent、智能客服等落地场景

  - 无需梯度更新的ICL落地思路可借鉴：用无标注人类演示样例做prompt即可提升任务完成率，降低小样本场景下的标注成本，适合垂类Agent的快速适配

  - 可参考其控制变量式消融实验设计：通过对比不同上下文输入（演示/反馈/标注）的效果增益，指导业务Agent的prompt工程与输入优化'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有机器人策略无法实现部署阶段的In-Context Learning，有限演示样本无法覆盖所有未知任务场景，如何利用VLM的通用能力实现无梯度更新的机器人任务泛化是具身AI落地的核心痛点。
### 方法关键点
提出GPT-Policy通用Agent框架，包含三个核心模块：1）上下文编译器，保留任务相关的视觉转换信息，过滤无关噪声；2）VLM模块，输出机器人工具动作提案；3）约束控制器，验证动作可执行性、执行并返回结果，全程无需梯度更新或任务专属参数调整。
### 关键结果
实机测试中，无机器人动作标注的人类视频演示可直接提升任务完成率，带对齐动作参考的样例可让接触敏感类任务的表现获得进一步提升，为VLM通用能力落地实体场景提供了实证支撑。
