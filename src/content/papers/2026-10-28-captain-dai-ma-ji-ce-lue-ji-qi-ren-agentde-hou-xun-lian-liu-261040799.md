---
title: 'CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents'
title_zh: CaPtain：代码即策略机器人Agent的后训练流水线
authors:
- Yijia Fan
- Xilin He
- Yilei Jiang
- Dongming Wu
- Jiaxu Wang
- Xiangyu Yue
affiliations:
- MMLab, The Chinese University of Hong Kong
- NovaXBot
arxiv_id: '2610.40799'
url: https://arxiv.org/abs/2610.40799
pdf_url: https://arxiv.org/pdf/2610.40799
published: '2026-10-28'
collected: '2026-11-02'
category: Agent
direction: 具身Agent · 代码即策略后训练
tags:
- Agent
- Code-as-Policy
- SFT
- Reinforcement-Learning
- VLM
one_liner: 提出端到端SFT+RL后训练流水线，将4B开源VLM训练为低成本高性能代码即策略机器人Agent
practical_value: '- 多轮Agent长序列决策的RL信用分配可借鉴不对称评论家方案：训练阶段引入业务侧特权状态（如推荐场景后台真实用户反馈、商品全量属性）做稠密信用赋值，推理阶段完全不依赖特权数据，大幅降低延迟奖励的分配噪声

  - 小参数模型对齐Agent交互协议可采用「大模型合成轨迹SFT + 业务场景RL」的两阶段范式：先用大模型批量生成符合交互格式的正样本做SFT对齐协议，再用RL优化业务目标，大幅降低小模型落地Agent的门槛

  - Agent执行层设计可参考统一低阶API+结构化回执的思路：把工具调用返回统一为结构化文本回执，同时内置上下文自动压缩机制，适配小模型有限的上下文窗口，降低业务适配成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Code-as-Policy（CaP）机器人Agent要么依赖闭源前沿大模型，推理成本高、不可定制微调，要么依赖冻结的VLA或高阶技能模块，性能被训练数据上限卡死；小开源VLM直接应用于CaP场景成功率几乎为0，缺少成熟的后训练方案将小VLM转化为独立可部署的CaP Agent。
### 方法关键点
- 设计CaPtain-Harness统一执行环境：仅暴露22个低阶感知、测量、运动原语API，无预定义高阶技能（如抓取、放置），每次调用返回结构化物理回执，跨仿真/真实机器人API完全一致，内置上下文自动压缩适配小模型有限窗口
- 两阶段后训练：第一阶段用GPT-6 Astra生成的仿真交互轨迹做SFT，对齐模型到交互协议，训练时随机掩码历史坐标强制模型grounding到当前图像；第二阶段做多轮RL，训练时用仅评论家可见的仿真特权物理状态做稠密每步信用赋值，推理时移除评论家，仅靠图像和回执决策
- 信用分配优化：用模拟器评论家预测的任务成功率时序差作为每步奖励，仅对改变物理状态的动作（如抓取、移动）分配高信用，感知类请求信用接近0，解决长序列延迟奖励的分配噪声问题
### 关键结果
基于Qwen3.5-4B训练的CaPtain-4B，LIBERO基准零-shot成功率从0提升至SFT后的55.4%，RL后达73.8%；LIBERO-PRO上达78.5%，超过K1、WAA等多个前沿闭源模型Agent，RL增益在3个扰动测试集上保持17.6~21.2个百分点；零-shot迁移到SimplerEnv WidowX达83.3%，CaP-Bench达75%，均超过部分闭源大模型，单episode推理成本仅0.03~0.06美元，比闭源方案低1~2个数量级。
> 值得记住的话：小参数VLM只要对齐统一的执行环境协议，搭配合理的SFT+RL训练方案，就能在特定场景下达到甚至超过闭源大模型Agent的性能，同时推理成本低两个数量级。
