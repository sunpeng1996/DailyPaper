---
title: What AI Red-Team Evaluations Can and Cannot Prove
title_zh: AI红队评估的可证明与不可证明边界
authors:
- Bandana Kaur
affiliations:
- APIsec Research Labs
arxiv_id: '2607.21735'
url: https://arxiv.org/abs/2607.21735
pdf_url: https://arxiv.org/pdf/2607.21735
published: '2026-07-22'
collected: '2026-08-07'
category: Eval
direction: AI安全评估 · 红队测试边界量化
tags:
- Red-Team
- AI Safety
- Evaluation Bound
- Evidential Ceiling
- Risk Assessment
one_liner: 定义AI红队评估的证据上限，量化其对不同风险等级危害的证明能力边界
practical_value: '- 内部测试LLM4Rec、电商Agent服务的合规风险时，可复用证据上限公式量化测试集规模是否足够验证高频风险（如推荐违禁品、话术违规）

  - 针对极低概率的灾难性风险（如大促推荐触发大规模合规事故），不要依赖常规红队测试结果，需额外设计针对性强化测试流程

  - 做模型上线前的安全评估时，先按风险发生频率分类：高频风险用标准红队基准即可，低频高损风险需补充自适应攻击测试'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有AI红队评估的证明能力无明确量化边界，产业与监管广泛依赖的安全测试结果，对低概率高危害风险的参考价值模糊。
### 方法关键点
定义评估的证据上限为固定测试预算下测试结果可改变信念的最大系数，推导闭式解明确两类评估 regime 的分界点；框架同时覆盖被动基准、自适应/自动化红队场景，核心评估依据为假设区分度而非攻击成功率。
### 关键结果数字
审计8套主流评估套件发现，当前基准仅能覆盖高频危害类别，对罕见灾难性风险的测试能力差数个数量级；分界点随测试样本量n呈1/n下降，高于临界危害率时，干净测试结果比单次复现的故障更有说服力，低于临界值时可行规模的被动基准无法提供足够安全证据。
