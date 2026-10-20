---
title: 'TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents'
title_zh: 《TokenEconomizer：面向编码Agent的经验驱动黑盒成本控制方法》
authors:
- Aaron J. Li
- Weijia Xu
- Chandan Singh
- Zixiao Chen
- Jeevana Priya Inala
- Charlotte Siska
- Acar Tamersoy
- Bin Yu
- Ion Stoica
- Michel Galley
affiliations:
- UC Berkeley
- Microsoft Research
- Microsoft Security
arxiv_id: '2610.22732'
url: https://arxiv.org/abs/2610.22732
pdf_url: https://arxiv.org/pdf/2610.22732
published: '2026-10-14'
collected: '2026-10-20'
category: Agent
direction: Agent成本优化 · 黑盒自适应控制
tags:
- Agent
- Cost Optimization
- LLM
- Black-box Control
- Token Efficiency
one_liner: 黑盒外挂控制器基于历史轨迹自适应优化编码Agent配置，降低token成本18.4~30.9%且任务成功率接近基准
practical_value: '- 可复用黑盒外挂设计思路，无需修改现有Agent核心逻辑，仅通过干预prompt、工具集、执行中断三个控制点即可实现成本优化，大幅降低业务落地改造成本

  - 跨任务经验复用的三个策略可直接迁移：从历史轨迹提炼领域微技能注入prompt、裁剪长期未用工具、基于历史成功轨迹的轮次阈值做失败环路干预，多场景下均有稳定收益

  - 可借鉴「先验证有用再激活、出错快速回退」的策略设计：微技能需多次验证有效才注入，裁剪的工具定期恢复审计，失败干预先重定向再终止，平衡成本优化和任务成功率

  - 电商/推荐场景的Agent服务（如智能客服、运营文案生成Agent、选品Agent）可直接套用该框架优化token消耗，同领域多任务连续执行场景收益更明显'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent的token效率优化多针对单孤立任务，未考虑实际生产中同环境（如同代码库、同业务场景）下连续执行多任务时的重复成本；固定成本优化策略在不同环境下效果波动大，甚至会升高成本，同时现有方法多需修改Agent核心逻辑或模型，落地成本高。

### 方法关键点
- 完全黑盒设计，不修改Agent模型、代码与核心逻辑，仅通过调整prompt前缀、加载工具集、实时执行控制三个入口实现干预
- 三大核心自适应策略：1）微技能注入：从历史完成轨迹提炼短操作经验，经多任务验证有效且需求率达标才注入prompt前缀，失效后自动下线；2）工具裁剪：保留核心读写执行工具，裁剪连续多任务未使用且LLM判定无关的工具，定期恢复全工具集审计；3）失败环路干预：基于历史成功任务的轮次百分位设置预算，检测到重复失败签名时先引导重试，无效再终止

### 关键结果
在SWE-Bench（277个任务）、Web-Bench（102个任务）、两个安全审计基准（200个任务）上，对比Claude Code、Codex、GitHub Copilot CLI三类主流编码Agent，TokenEconomizer在成功率基本持平的前提下，SWE-Bench场景降本18.4~30.9%，Web开发场景降本16.0~21.2%，安全审计场景降本6.4~19.6%，所有测试的仓库-模型组合下均实现成本下降，且占据成本-质量帕累托最优区间。

**最值得记住的一句话**：同环境下连续执行多任务的Agent，通过经验驱动的黑盒自适应控制，可在几乎不损失效果的前提下实现稳定的token成本降低，且落地改造成本极低
