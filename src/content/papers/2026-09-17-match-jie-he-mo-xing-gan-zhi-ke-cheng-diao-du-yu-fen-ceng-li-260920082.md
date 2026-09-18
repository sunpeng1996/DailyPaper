---
title: 'MATCH: Model-Aware Tool Learning with Curriculum Scheduling and Hierarchically
  Gated Rewards'
title_zh: MATCH：结合模型感知课程调度与分层门控奖励的工具学习框架
authors:
- Shihao Liu
- Hao Yin
- Lijun Liu
- Zhengzong Chen
- Yuanyuan Zhao
- Fei Huang
affiliations:
- University of the Chinese Academy of Sciences
- Honor Device Co., Ltd
arxiv_id: '2609.20082'
url: https://arxiv.org/abs/2609.20082
pdf_url: https://arxiv.org/pdf/2609.20082
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: Agent 工具调用能力RL优化
tags:
- Tool Learning
- Reinforcement Learning
- Curriculum Learning
- Reward Design
- GRPO
one_liner: 提出结合模型感知课程调度与分层门控奖励的RL工具学习框架，在两大基准上精度大幅领先现有基线
practical_value: '- 工具调用类Agent的奖励设计可复用HTGR分层门控逻辑，比如电商导购Agent调用优惠券/库存查询工具时，仅工具名正确才发放参数层级奖励，避免虚假信用分配

  - RL训练采样可借鉴MACL动态难度调度策略，比如优化LLM排序/推荐Prompt时，动态选择靠近模型当前能力边界的样本，避免固定难度课程漂移失效，提升训练效率

  - MATCH闭环框架无需修改原生GRPO逻辑，适配多backbone，可直接迁移到电商导购Agent、广告投放Agent的工具调用能力迭代'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前RL-based工具学习存在两大核心痛点：一是固定阈值的课程调度无法匹配模型训练过程中动态变化的能力边界，训练数轮后采样区间就偏离有效区域；二是加和式细粒度奖励忽略工具调用的层级依赖逻辑，工具名错误时参数正确仍能拿到不合理奖励，导致信用分配泄露，训练效率和最终精度均受限。

### 方法关键点
- 模型感知课程学习（MACL）：基于当前HTGR奖励动态计算样本难度，每轮优先选取靠近模型能力边界的样本，同时补充一定比例更难样本，兼顾能力巩固与边界拓展，难度用EMA平滑降低波动。
- 分层工具调用门控奖励（HTGR）：按工具名、参数键、参数值顺序设置门控，仅前一级完全正确时才发放后一级奖励，同时加入格式校验辅助奖励，避免虚假信用；奖励信号同时用于GRPO更新和MACL难度刷新，形成闭环。
- 基于原生GRPO做策略更新，无需修改目标函数，适配性强。

### 关键实验结果
在API-Bank、BFCL V3两大工具学习基准测试，对比SFT、ToolRL、ToolSample等主流基线：MATCH在API-Bank整体精度达72.19%，较最强基线高7.2pp；在BFCL V3整体精度达62.87%，较最强基线高2.62pp，高难度L3、多轮调用场景增益尤为突出，且在Qwen、Llama两大模型族4款不同尺寸backbone上均实现稳定提升。

### 最值得记住的一句话
工具调用的RL优化需同时匹配训练样本难度与模型当前能力，且奖励设计必须贴合任务本身的依赖逻辑，才能最大化训练效率与最终效果
