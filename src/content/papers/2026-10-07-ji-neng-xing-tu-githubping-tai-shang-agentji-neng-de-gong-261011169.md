---
title: 'Skill Constellations: Tracing the Supply Chain of Agent Skills on GitHub'
title_zh: 《技能星图：GitHub平台上Agent技能的供应链追踪研究》
authors:
- Fahd Seddik
affiliations:
- University of British Columbia, Okanagan, Canada
arxiv_id: '2610.11169'
url: https://arxiv.org/abs/2610.11169
pdf_url: https://arxiv.org/pdf/2610.11169
published: '2026-10-07'
collected: '2026-10-10'
category: Agent
direction: Agent技能供应链安全与溯源优化
tags:
- Agent Skill
- Software Supply Chain
- GitHub Security
- Skill Diffusion
- Audit Ranking
one_liner: 构建首个带时间戳的Agent技能拷贝传播网络，实现高风险技能源头仓库高效审计排序
practical_value: '- 内部Agent技能库可复用拷贝传播追踪方案，建立技能血缘与版本溯源机制，避免无版本拷贝带来的安全/性能隐患

  - 内部技能生态审计可借鉴源头仓库排序模型，替代星标/热度排序，提升高风险问题拦截效率

  - 对外分发Agent技能包时优先采用版本化引用而非静态拷贝，确保缺陷修复可触达所有下游使用方'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有Agent技能通过仓库拷贝共享，无注册、版本和溯源机制，单点快照类研究无法追踪拷贝流向，高风险技能漏洞修复触达率极低，无法定位需优先审计的源头仓库。

### 方法关键点
基于GitSkills全量SKILL.md的git提交历史构建首个带时间戳的Agent技能拷贝网络，覆盖GitHub全平台219万+次技能采纳，配套交互式可视化查看器，拟合拷贝源选择模型实现高风险源头仓库排序。

### 关键结果数字
仅少量仓库是绝大多数技能拷贝的源头，GitHub星标无法识别这类核心仓库；源端修复仅能触达极少量拷贝副本；审计模型排序前100的仓库可拦截14.9%的后续高风险技能采纳，远高于星标Top100的0.5%拦截率。
