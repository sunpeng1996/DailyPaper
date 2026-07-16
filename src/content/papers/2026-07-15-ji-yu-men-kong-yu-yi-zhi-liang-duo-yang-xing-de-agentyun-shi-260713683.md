---
title: Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity
title_zh: 基于门控语义质量多样性的Agent运行时套件自进化框架
authors:
- Xiaotian Luo
- Fengxingyu Wang
- Chuanrui Hu
- Dizhan Xue
- Yafeng Deng
affiliations:
- EverMind AI
- Shanda Group
arxiv_id: '2607.13683'
url: https://arxiv.org/abs/2607.13683
pdf_url: https://arxiv.org/pdf/2607.13683
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent运行时套件自进化优化
tags:
- Self-Evolving-Agent
- Harness-Optimization
- GSME
- Quality-Diversity
- Generalization
one_liner: 分离Agent harness优化的提案与可信验证环节，通过GSME存档解决自进化过拟合问题
practical_value: '- 做业务Agent优化时可拆分语义提案与统计验证：LLM仅负责诊断故障、生成harness优化方案，所有效果验证由确定性代码执行配对2σ显著性检验，避免自反馈噪声与过拟合，可直接用于电商导购Agent、客服Agent的prompt/工具链优化

  - 优化方案按「修改位置（prompt/知识/运行时/配置）× 解决的故障类型」归档，不按任务归档，可天然降低过拟合风险，还支持跨故障类型的方案组合，适合推荐系统query理解Agent、多轮对话Agent的故障库建设

  - 评估时采用分层策略：先用小样本锚点集淘汰明显无效的候选，再跑全量验证，搭配树感知分数借用复用历史评估数据，可最多减少67%的评估成本，适配业务侧资源受限的迭代场景

  - 无需追求通用harness优化方案：不同模型的核心故障分布不同，只需匹配对应修复补丁即可，可迁移的是「诊断-提案-验证」的闭环流程而非具体补丁，换LLM底座时可快速重新迭代适配'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM Agent的实际性能由底座模型与周边运行时套件（harness，包括prompt、注入知识、控制流、配置等）共同决定，部署场景下模型权重通常固定（闭源、租赁或重训成本过高），自动优化harness是提效的核心路径。但现有自进化方法依赖噪声较大的自反馈，优化结果容易过拟合训练任务，无法验证增益的真实性和泛化性。

### 方法关键点
- 拆分提案与可信验证：用能力更强的Evolver LLM诊断现有Agent的失败轨迹，生成harness补丁，所有采样、效果统计、显著性判断完全由确定性代码完成，完全避免LLM的定量计算误差
- 提出GSME（门控语义MAP-Elites）存档：所有补丁按「修改位置（where：prompt/知识/运行时/配置）× 解决的故障类型（why）」归档，而非按对应任务归档，天然带抗过拟合偏置，支持跨单元的补丁组合
- 三层门控验证：有效性门（过滤沙箱、验证器等环境错误）、激活门（补丁实际触发才计入效果）、配对2σ显著性门（排除随机波动导致的虚假增益），优化全程不接触测试集，最终效果仅在密封测试集上打分1次

### 关键实验
在7个跨领域基准（代码、数学、网页操作、APP操作等）上用固定权重的Qwen3.6-27B验证，基线为原始harness，密封测试集上的增益达9~15.5pp，保留了训练集增益的86%~147%，无过拟合现象；跨模型测试表明，最优补丁完全匹配对应模型的核心故障类型，相同故障-补丁的对应关系可跨Qwen、Gemini两个模型家族复用。

### 最值得记住的一句话
可迁移的不是某一个最优harness补丁，而是「诊断故障-生成补丁-可信验证」的自进化闭环本身。
