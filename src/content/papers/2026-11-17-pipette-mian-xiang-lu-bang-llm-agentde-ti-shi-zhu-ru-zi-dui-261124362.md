---
title: 'PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents'
title_zh: PIPETTE：面向鲁棒LLM Agent的提示注入紫队攻防框架
authors:
- Lipeng He
- Yihan Wang
- Jiawen Zhang
- N. Asokan
affiliations:
- University of Waterloo
- Zhejiang University
- KTH Royal Institute of Technology
arxiv_id: '2611.24362'
url: https://arxiv.org/abs/2611.24362
pdf_url: https://arxiv.org/pdf/2611.24362
published: '2026-11-17'
collected: '2026-11-19'
category: Agent
direction: LLM Agent 提示注入攻防优化
tags:
- LLM Agent
- Prompt Injection
- Red Teaming
- Adversarial Training
- Robustness
one_liner: 提出兼顾攻击策略多样性和防御效用的提示注入紫队框架，大幅降攻击成功率同时保留业务效用
practical_value: '- 业务Agent上线前做红队测试时，不要只追求攻击成功率（ASR）指标，可加入策略多样性奖励避免模式collapse，否则后续对抗训练后仍防不住未知攻击

  - 对抗训练阶段可复用token级自蒸馏奖励设计，替代全轨迹二元奖励，既能提升鲁棒性又不会让Agent过度谨慎拒答，适配电商导购/客服Agent不能随意中断用户任务的场景

  - 若业务Agent需要接入外部非信任数据（如用户评论、第三方商品信息、工具返回结果），可直接复用这套紫队流程做离线攻防演练后再上线，提前规避提示注入风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于RL的提示注入红队方法仅优化攻击成功率（ASR），会出现策略级模式崩溃：反复生成同一攻击策略的表面改写版本，后续用这些样本做对抗训练，仅能修复单一漏洞，防不住未知攻击；同时传统对抗训练用全轨迹二元奖励，容易让Agent变得过度谨慎，大幅降低正常任务完成率，无法满足业务可用性要求。

### 方法关键点
1. **红队阶段（PIPETTE-Red）**：引入字典学习的策略覆盖奖励，定期更新攻击策略字典，仅成功且未被字典覆盖的新策略能获得高奖励，引导红队生成更多元的攻击，避免模式collapse
2. **蓝队训练阶段（PIPETTE-Blue）**：先通过SFT暖身让Agent学会行动前做安全检查推理，再组合轨迹级防御奖励、CoT推理奖励、正负前缀引导的token级自蒸馏奖励，精准分配信用，避免Agent过度拒答

### 关键实验
在AgentDojo、ASB两个跨域基准上测试，对比RL-Hammer、PISmith等红队基线，以及Meta-SecAlign、SecOPD等防御基线：静态攻击下ASR接近0；迭代自适应攻击下ASR最低到0%（Llama-8B），最高仅10%（GPT-OSS-20B）；同时正常任务效用（BU）比基线高3~15个百分点，甚至略优于未防御的原始模型。

> 最值得记住的一句话：红队测试的核心价值不是刷高攻击成功率，而是覆盖尽可能多的攻击策略，才能真正转化为防御后的鲁棒性提升
