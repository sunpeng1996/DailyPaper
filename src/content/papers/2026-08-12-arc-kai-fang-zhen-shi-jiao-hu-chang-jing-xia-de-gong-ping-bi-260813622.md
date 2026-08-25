---
title: 'ARC: Fair Relative Advantage Comparison in Open-Ended Real-World Interaction'
title_zh: ARC：开放真实交互场景下的公平相对优势比较方法
authors:
- Yongqi Tong
- Tan Li Hui Faith
- Choy Zhen Wen Marcus
- Zhou Jin
- Kewei Fu
- Jiang-Ming Yang
- Jianshe Li
- Xin Zhang
affiliations:
- Ant International
arxiv_id: '2608.13622'
url: https://arxiv.org/abs/2608.13622
pdf_url: https://arxiv.org/pdf/2608.13622
published: '2026-08-12'
collected: '2026-08-25'
category: Agent
direction: Agent 交互策略与RL训练优化
tags:
- Agent
- RLHF
- Tool Use
- GRPO
- Reward Fairness
one_liner: 提出策略分组RL训练方法ARC与通道分离交互框架INTER3，解决开放交互下奖励比较不公平问题
practical_value: '- 电商/客服/导购Agent可复用INTER3的三通道分离设计，通过<answer>标签拆分用户可见内容、内部推理、工具调用，实测可将TTFT从4.91s降至1.27s，大幅提升实时交互体验

  - 做Agent RLHF训练时可借鉴ARC思路：对有多种合法交互策略的场景，训练时按策略标签对rollout分组，仅同组内计算相对优势，避免奖励模型风格偏好带偏优化方向，推理时无需额外标签

  - 构建交互Agent训练数据集时，可复用INTER3-86K的双大模型预标注+人工校验的策略标注流程，低成本生成策略标注样本

  - 多通道输出Agent的RL训练可添加熵正则化，避免输出坍缩为无意义的重复<answer>块，保证多策略探索的多样性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
开放真实交互场景（如电商客服、导购、工具调用Agent）中，同一用户请求通常存在多种合法交互策略（直接回答、先澄清信息、操作前确认、执行中同步进度），传统分组RL（如GRPO）将不同策略的rollout混合计算相对优势，会被奖励模型的风格偏好（如偏好长回复、特定表述）干扰，导致优化向奖励偏好的策略倾斜，而非适配上下文的最优策略，最终降低工具调用准确率、损害用户体验。
### 方法关键点
- **ARC训练范式**：训练时给每个样本绑定交互策略标签，仅在相同策略的rollout组内计算相对优势，配合混合奖励与熵正则化更新策略；推理时移除策略标签，由模型自主选择最优交互策略
- **INTER3交互框架**：拆分三类输出通道：<answer>标签包裹内容直接推送给用户，其余文本为内部推理，工具调用为结构化内部动作，支持用户打断、实时进度推送，解决传统think-then-act模式首token延迟高的问题，同时让交互策略可观测、可标注
- **INTER3-86K数据集**：融合真实线上交互日志、公开基准重写数据、大模型合成数据，共86.8K样本，覆盖4大类9小类交互策略，支持SFT与RL训练
### 关键结果
- 对比纯GRPO基线，ARC+GRPO在τ/τ2工具调用基准上平均提升5.37分，其中τ-airline准确率从31.33升至44.00，τ-retail从40.29升至50.00
- INTER3相比think-style基线，TTFT从4.91s降至1.27s，同时不损失工具调用能力
- 4B小模型上ARC依然生效，工具调用平均得分比4B no-think基线高53%

开放交互Agent训练的核心瓶颈不止是奖励信号质量，更在于不同行为的比较是否公平
