---
title: 'One Task, Many Interfaces: Simple Cross-Interface Consistency Training Improves
  LLM Agent Robustness'
title_zh: 跨接口一致性训练提升LLM Agent工具调用的鲁棒性
authors:
- Artin Tajdini
- Manpreet Kaur
- Peng Qi
affiliations:
- University of Washington
- Uniphore
arxiv_id: '2610.20576'
url: https://arxiv.org/abs/2610.20576
pdf_url: https://arxiv.org/pdf/2610.20576
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: Agent 工具调用鲁棒性优化
tags:
- LLM Agent
- Tool Calling
- Consistency Regularization
- Robustness
- Policy Training
one_liner: 提出跨接口策略正则化CIPR，无需枚举所有接口扰动即可提升LLM Agent工具调用鲁棒性
practical_value: '- 工具调用类Agent训练可复用CIPR的接口正则化思路：先做接口规范化（将工具/操作名替换为无意义标识符），再搭配双接口KL约束，不损失原有精度的前提下降低对接口命名、排序的依赖，适合电商导购Agent、客服Agent这类工具/API频繁迭代的场景

  - 电商推荐系统的多端一致性训练可借鉴：同一用户意图在不同端（APP/小程序/PC）的交互入口命名、排序不同时，可引入类似的跨入口行为分布KL正则，降低多端迁移的效果损耗

  - 低资源Agent微调可复用rescoring一致性KL实现：无需额外生成rollout，仅对现有标注样本做接口重标记即可计算正则项，训练成本提升极小，适合业务场景快速迭代Agent能力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM Agent的工具调用能力高度绑定训练时的接口格式，工具重命名、排序、新增等价工具这类语义不变的接口扰动，会导致Agent准确率骤降25%左右；传统多接口随机训练只能拟合见过的扰动，对未见过的分布外扰动泛化性差，而业务场景中API迭代、工具提供商变更属于常态，亟需不依赖枚举扰动的鲁棒训练方法。

### 方法关键点
1. 接口规范化：训练&推理时均将工具名、参数名替换为中性无意义标识符（如function_01、arg_01），仅保留工具描述、参数类型等核心语义信息，推理时通过适配器做接口名映射，完全屏蔽命名shortcut
2. 双接口构造：每个训练样本构造一对等价接口，原始为规范化接口，扰动接口新增工具降级副本、重命名所有工具、打乱工具/参数排序，天然掌握两个接口的等价工具对应关系
3. 双一致性正则：① rescoring一致性KL：固定已生成的回复，仅重标记接口名后计算动作分布的KL，无额外生成成本；② rollout一致性KL：两个接口分别生成回复，计算平均动作分布的KL，允许推理逻辑差异，两个正则项加在原有任务损失上，无需额外标注

### 关键结果
在BFCL工具调用数据集上，对比基线GRPO训练的Agent，CIPR在原有接口准确率无损失的前提下，未见过的接口扰动下平均准确率提升15.5个百分点（Qwen2.5-3B），原有25%的准确率损失可恢复10.5个百分点；在WebShop任务上做自蒸馏后，Agent对动作重命名的鲁棒性从5.5%提升到76%。

**最值得记住的一句话**：Agent训练时不能只要求单接口下结果正确，还要约束语义等价的不同接口下的动作分布一致，才能从根源降低对界面shortcut的依赖
