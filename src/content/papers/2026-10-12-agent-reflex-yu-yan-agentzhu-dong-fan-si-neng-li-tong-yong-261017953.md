---
title: 'Agent-Reflex: Teaching Language Agents to Act Reflectively'
title_zh: Agent-Reflex：语言Agent主动反思能力通用训练框架
authors:
- Guanting Dong
- Xinyu Yang
- Jiajie Jin
- Yuyang Hu
- Xiaoshuai Song
- Yifei Chen
- Xiaoxi Li
- Jiejun Tan
- Yutao Zhu
- Tat-Seng Chua
affiliations:
- Renmin University of China
- National University of Singapore
arxiv_id: '2610.17953'
url: https://arxiv.org/abs/2610.17953
pdf_url: https://arxiv.org/pdf/2610.17953
published: '2026-10-12'
collected: '2026-10-14'
category: Agent
direction: Agent 主动反思能力训练优化
tags:
- Agent Training
- Reflection Learning
- Tool Use
- Noise Robustness
- Reinforcement Learning
one_liner: 提出三阶段语言Agent主动反思训练框架，提升长周期工具调用与噪声环境表现
practical_value: '- 可复用RSD阶段的「真实错误注入+成功/失败轨迹对挖掘元技能」思路，用于电商导购、广告投放Agent的故障容错训练，比如将API超时、权限错误等真实故障注入训练环境，挖掘对应恢复规则

  - 可直接复用ReSFT的三类反思采样策略（局部自修复、全局重规划、用户引导修正）构造微调数据，优化业务Agent应对用户中途改需求、工具返回异常的表现

  - ORPO的「RL + 反思元技能引导token级蒸馏」范式可迁移到推荐系统Agent在线优化，不增加推理耗时即可提升决策鲁棒性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent训练多基于无噪环境假设，未覆盖真实部署中工具返回噪声、用户中途纠错的场景，导致Agent故障恢复能力弱；推理时的反思方法依赖动态生成的提示，可靠性差，缺乏可复用的系统化反思能力训练方案。

### 方法关键点
- 阶段1 环境反思技能发现（RSD）：基于557个真实MCP服务构造可执行环境，注入8类真实工具错误，从多模型采样的轨迹中挖掘1170条环境级可复用反思元技能
- 阶段2 反思监督微调（ReSFT）：基于元技能构造三类微调数据：自反思采样（局部修复错误）、技能恢复采样（全局重规划）、用户中心反思采样（响应人类纠错），合并后做SFT内化技能
- 阶段3 在线反思策略优化（ORPO）：结合噪声环境下的Agent RL，加入反思元技能引导的同token打分对比做token级蒸馏，用置信度加权稳定训练

### 关键结果
基于Qwen3-8B训练，在5个长周期工具调用基准上整体得分58.6，超过所有7-8B基线；在噪声基准AgentNoiseBench得分29.1，比次优NoisyAgent-8B高3.2个点；100步RL训练后效果持续优于GRPO、SEED等主流RL算法，训练过程更稳定。

### 核心结论
把反思从推理时的临时策略转化为可训练的元技能，从真实故障轨迹中挖掘可复用规则，才能让Agent在真实部署的噪声环境下稳定执行任务。
