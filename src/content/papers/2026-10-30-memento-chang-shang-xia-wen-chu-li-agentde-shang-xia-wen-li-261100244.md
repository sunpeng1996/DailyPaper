---
title: 'MEMENTO: Learning Context Management for Long Context Processing Agents'
title_zh: MEMENTO：长上下文处理Agent的上下文管理学习方法
authors:
- Yunfan Zhang
- Taehoon Hwang
- Kathleen McKeown
- Smaranda Muresan
affiliations:
- Columbia University
arxiv_id: '2611.00244'
url: https://arxiv.org/abs/2611.00244
pdf_url: https://arxiv.org/pdf/2611.00244
published: '2026-10-30'
collected: '2026-11-03'
category: Agent
direction: Agent长上下文处理 · 记忆管理
tags:
- LLM Agent
- Context Management
- Long Context Processing
- SFT
- RL
- Question Answering
one_liner: 基于SFT+RL训练Qwen3-8B Agent，通过笔记压缩实现低成本长上下文处理，性能追平百倍大模型
practical_value: '- 电商/搜索推荐多轮Agent可借鉴事后标注笔记的SFT初始化方案：用大模型生成历史交互的高质量总结样本，小模型快速习得上下文压缩能力，解决纯RL难探索有效记忆策略的问题

  - 多轮推荐/用户长会话建模可复用混合奖励设计：结合格式合规、记忆有效性、推荐结果正确性、置信度校准的多维度奖励，避免RL训练中的奖励黑客问题

  - 业务落地可灵活适配推理策略：仅需训练最基础的单窗口上下文压缩能力，即可零额外成本适配上下文折叠、置信度引导回溯等进阶逻辑，可根据成本-精度需求自由切换，大幅降低训练复杂度'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有长上下文LLM推理成本极高，且长输入下性能衰减明显；常规ReAct范式Agent会不断累积思考、动作、观测到上下文，最终超出窗口限制，单纯prompt无法引导大模型生成有效的压缩笔记，纯RL也很难探索出有用的记笔记行为，亟需低成本的长上下文Agent上下文管理方案。
### 方法关键点
- SFT初始化：收集大模型生成的正确任务轨迹，事后插入符合频率、位置、多样性规则的压缩笔记，用这批合成轨迹微调小模型，先教会模型正确的记笔记行为范式
- RL优化：采用GRPO算法，混合奖励覆盖格式合规、笔记有效性、回答正确性、置信度校准四个维度，跨上下文窗口统一计算整条轨迹的优势，让早期记笔记动作也能获得最终结果的反馈信号
- 训练-推理解耦：训练仅用最简单的单窗口压缩逻辑，推理可无缝适配上下文折叠、置信度引导回溯两种进阶策略，几乎无训练测试偏差
### 关键结果
在4个书籍级QA数据集共4.7K测试样本上，基于Qwen3-8B的MEMENTO准确率达67.8%，较基线Qwen3-8B Agent提升30.9个百分点，追平100倍参数量的GLM-5.3 Agent（69.3%），推理成本仅为后者1/9；较全上下文输入的GLM-5.3仅低6.4个百分点，成本低26倍；同时远超全上下文输入的GPT-5.5的56.7%，成本仅为后者1/54。
### 最值得记住的一句话
上下文管理是需要和任务、推理框架联合学习的行为，而非靠prompt或者模型规模就能自发涌现的能力，小模型经过针对性训练可在长上下文任务上获得极高的性价比。
