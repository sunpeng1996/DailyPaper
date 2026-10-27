---
title: Steering Black-Box Large Language Model Agents with Pitfall Anticipation World
  Model
title_zh: 基于陷阱预判世界模型（PAWM）的黑盒LLM Agent引导方法
authors:
- Jiongxiao Wang
- Han Ding
- Youzhi Luo
- Yawei Wang
- Yun Zhou
- Linbo Liu
- Panpan Xu
affiliations:
- University of Wisconsin–Madison
- AWS AI
arxiv_id: '2610.29139'
url: https://arxiv.org/abs/2610.29139
pdf_url: https://arxiv.org/pdf/2610.29139
published: '2026-10-20'
collected: '2026-10-27'
category: Agent
direction: Agent 黑盒LLM引导·世界模型优化
tags:
- LLM Agent
- World Model
- Black-box LLM
- GRPO
- SFT
one_liner: 通过仅在陷阱节点介入的轻量化世界模型，大幅提升黑盒LLM Agent任务成功率
practical_value: '- 电商导购、订单履约类黑盒LLM Agent无需微调商用基座权重，可训练轻量化PAWM作为辅助模块，仅在用户/Agent动作即将踩坑时介入，兼顾效果与合规性

  - 借鉴“仅陷阱节点调用”的设计，可将世界模型/外部引导模块的调用量降低60%以上，大幅降低高并发业务场景下的API与推理成本

  - 训练辅助引导模型可复用两阶段范式：先用成功/失败轨迹对比生成的合成数据做SFT，再用GRPO和黑盒基座联合调优，无需人工标注即可快速对齐业务场景需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有黑盒LLM Agent（如GPT、Claude）仅具备通用推理能力，无法内化特定任务的环境动态，传统世界模型方案要么每步预测下一个观测，调用成本极高，要么输出全路径预测累积误差大，多数引导不仅无法帮助Agent，甚至会产生负向干扰，大幅降低任务成功率。
### 方法关键点
- 先通过试点实验明确两个核心设计原则：世界模型仅在预判多步内会出现任务陷阱时介入，且输出到下一个子目标的预判路径时效果最优，调用成本仅为全量介入的1/3左右
- 两阶段训练PAWM：第一阶段用合成轨迹数据做SFT，通过对比同任务成功/失败轨迹自动定位坑点，同时对无坑的`<pass>`样本做降采样，避免模型倾向于沉默不输出引导；第二阶段用GRPO和冻结的黑盒LLM Agent联合训练，基于最终任务奖励优化预判的准确性与引导的有效性
- 推理时PAWM预判无坑直接输出`<pass>`，不干扰Agent原有决策，仅在有坑时输出预警和修正引导，让Agent重新生成动作
### 关键实验
在ScienceWorld和WebArena-Lite两个主流Agent基准上测试，引导Claude Sonnet 4.5时，比无引导基线分别提升24.3%、7.7%的任务成功率，分别达78.9%、80.4%，同时PAWM学到的陷阱知识可跨基座迁移到Haiku、GLM 5等不同LLM。
### 核心结论
给黑盒LLM Agent做外部引导，不需要全步骤干预，只要精准命中其会踩坑的关键节点给出指导，就能用最低成本拿到最大收益。
