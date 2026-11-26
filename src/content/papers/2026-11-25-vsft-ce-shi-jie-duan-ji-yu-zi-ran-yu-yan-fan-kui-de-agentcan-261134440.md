---
title: 'vSFT: Learning to Verbally Tune Agents at Test Time'
title_zh: vSFT：测试阶段基于自然语言反馈的Agent参数调优框架
authors:
- Qishuai Wen
- Rui Chen
- Haiwen Li
- Zhiyuan Huang
- Qiwen Gu
- Bingjie Gao
- Geng Li
- Jing Tang
- Xiangxiang Chu
- Chun-Guang Li
affiliations:
- Alibaba Group AMAP
- Shenzhen Loop Area Institute
- Tongji University
- Shanghai Jiao Tong University
- Independent Researcher
arxiv_id: '2611.34440'
url: https://arxiv.org/abs/2611.34440
pdf_url: https://arxiv.org/pdf/2611.34440
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: Agent测试时自适应 · 语言监督转LoRA更新
tags:
- vSFT
- LoRA
- HyperNetwork
- Test-time Adaptation
- LLM Agent
one_liner: 提出vSFT框架，通过超网络将语言监督转为LoRA更新，测试时闭环迭代调优Agent
practical_value: '- 电商导购/搜索意图理解Agent可复用该闭环逻辑，将用户负反馈、运营规则转为自然语言监督，通过超网络生成LoRA快速适配，避免反复全量SFT，降低迭代成本

  - 生成式推荐场景可将用户点击/退款等行为的自然语言归因分析，通过超网络转为LoRA更新，快速修正推荐策略，解决in-context提示生效不稳定的问题

  - 工程上可复用其轻量超网络设计，仅421M参数即可生成适配大模型的LoRA，训练rollout预算仅为GRPO的4%-10%，成本远低于RL类方法

  - 多场景适配时可借鉴其LoRA合并思路，将单场景优化LoRA合并为通用适配层，跨场景迁移效果优于in-context skill bank'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent调优方法存在明显缺陷：SFT分布偏移大、golden轨迹难获取；RL类方法rollout成本高、奖励稀疏；vRL类in-context反馈依赖上下文窗口，长任务生效不稳定，且无法沉淀为参数优化，亟需测试时高效、可靠的自适应机制。

### 方法关键点
- 构建Agent-监督器-超网络的闭环迭代流程：Agent与环境交互产出失败轨迹后，监督器生成自然语言形式的技能、反思类反馈
- 超网络将系统提示、少样本示例、累计语言反馈转为LoRA适配器，直接更新Agent参数，无需反向传播，实现参数级而非上下文级的适配
- 超网络采用离线元训练：收集vRL框架下的成功轨迹，构建<条件-查询-响应>三元组数据集，通过交叉熵损失训练超网络生成能复现成功行为的LoRA

### 关键实验
在ALFWorld、WebShop两个Agent基准上测试，base模型为Qwen3-4B：相比Reflexion，ALFWorld成功率提升13.9%，WebShop成功率提升18.2%；相比GRPO，ALFWorld成功率提升8.7%、WebShop提升4.8%，rollout预算仅为GRPO的4%（ALFWorld）和10%（WebShop）；搭配Qwen-Plus作为监督器时，4B参数的Agent效果接近Qwen3.8-Max。

**最值得记住的一句话**：学习「如何自适应模型」，而非直接产出一个适配好的模型，是Agent实现自我进化的可行路径。
