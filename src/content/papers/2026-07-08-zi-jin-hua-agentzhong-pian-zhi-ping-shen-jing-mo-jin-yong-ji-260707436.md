---
title: 'The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in
  Self-Evolving Agents'
title_zh: 自进化Agent中偏置评审静默禁用劣质技能淘汰机制的机理研究
authors:
- Xing Zhang
- Yanwei Cui
- Guanghui Wang
- Ziyuan Li
- Wei Qiu
- Bing Zhu
- Peiyang He
affiliations:
- AWS Generative AI Innovation Center
- HSBC Holdings Plc., HSBC Technology Center, China
arxiv_id: '2607.07436'
url: https://arxiv.org/abs/2607.07436
pdf_url: https://arxiv.org/pdf/2607.07436
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: 自进化Agent · 技能库治理
tags:
- Self-Evolving Agent
- LLM-as-Judge
- Skill Retirement
- Library Drift
- Bias Audit
one_liner: 揭示自进化Agent技能淘汰机制的假正偏置失效阈值，提供上线前缺陷注入审计方案
practical_value: '- 构建电商/广告领域的自进化Agent（如文案生成、智能客服、选品Agent）时，优先审计LLM评审的false-pass rate，超过阈值(1-τ)/2不要开启自动技能淘汰，避免技能库静默劣化

  - 优化LLM评审时优先压低false-pass率，而非整体准确率：对称噪声（好技能误判为坏）对技能淘汰的影响可容忍，只有假正（坏技能误判为好）是致命的

  - 上线自进化模块前用低成本缺陷注入法做go/no-go测试：构造带已知缺陷的样本，测量评审漏判率，提前定位是否在安全区，无需等线上指标恶化

  - 监控技能库健康度不要只看总淘汰数，要拆分真实贡献驱动的淘汰和容量不足导致的驱逐churn，总淘汰数正常不代表淘汰机制在工作'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
自进化Agent依赖淘汰劣质技能避免技能库漂移，但该机制的无偏奖励假设在无参考生成任务（如商品文案、用户研究报告）中不成立：这类任务只能用LLM作为评审，其误差并非白噪声，假正偏置（失败结果被判通过）会导致淘汰机制静默失效，现有研究未覆盖该风险的机理与防控方法。
### 方法关键点
- 拆分评审误差为两类：对称噪声（双向随机误判）、假正偏置（仅失败误判为成功），理论推导得出假正偏置的失效阈值为ρ_F→P=(1-τ)/2，超过该阈值后无论多少数据都无法恢复淘汰能力
- 设计低成本缺陷注入审计方案：向正常输出注入已知缺陷，测量LLM评审的漏判率，上线前即可判定系统是否处于安全区
- 跨报告写作、代码生成两个领域做受控实验，拆分真实贡献驱动的技能淘汰与容量不足导致的驱逐churn，排除机制混淆
### 关键结果
在4个数据集（3个长文本报告类、1个MBPP+代码类）上验证：
1. 假正率超过0.45（对应τ=0.1）时，真实技能淘汰量直接降为0，而对称噪声哪怕达到0.4也不会导致淘汰机制失效
2. 中等假正率（0.45）时评估效果比干净奖励低6.5pct，极端假正率反而因技能合成也被饿死，效果回归基线，失效早期无明显整体指标下降，呈静默特征
### 核心洞见
自进化Agent的技能淘汰机制只会死于假正偏置，不会死于噪声，上线前做缺陷注入审计比堆数据调参数更有效
