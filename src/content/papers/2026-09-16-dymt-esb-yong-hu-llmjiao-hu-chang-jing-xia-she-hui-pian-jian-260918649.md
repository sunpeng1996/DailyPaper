---
title: 'DyMT-ESB: Dynamic Multi-Turn Evaluation of Social Bias in User-LLM Interactions'
title_zh: DyMT-ESB：用户-LLM交互场景下社会偏见的动态多轮评估
authors:
- Rem Hida
- Masahiro Kaneko
- Daisuke Oba
- Danushka Bollegala
- Naoaki Okazaki
affiliations:
- Institute of Science Tokyo
- MBZUAI
- Third Intelligence
- The University of Liverpool
arxiv_id: '2609.18649'
url: https://arxiv.org/abs/2609.18649
pdf_url: https://arxiv.org/pdf/2609.18649
published: '2026-09-16'
collected: '2026-09-17'
category: Eval
direction: LLM安全 · 多轮交互偏见评估
tags:
- LLM Safety
- Multi-turn Conversation
- Social Bias
- Evaluation Protocol
- Dynamic Testing
one_liner: 提出动态生成追问的可变轮次LLM社会偏见评估协议，揭示多轮交互下偏见的三类动态特征
practical_value: '- 搭建电商客服、导购类业务Agent的多轮安全检测体系时，可复用动态生成追问的可变轮次评估框架，替代固定脚本检测，覆盖晚现、复现类偏见问题，降低舆情风险

  - 做业务场景LLM对齐微调时，可新增多轮动态偏见检测用例，优化模型长对话场景下的安全性，避免电商个性化推荐、导购对话中出现性别/地域等偏见

  - 做多轮用户交互下的推荐系统建模时，可参考本文动态逐轮追踪特征的思路，捕捉用户兴趣的非单调、晚现、复现类变化规律，提升长会话推荐准确率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM多轮社会偏见评估依赖预定义模板输入、固定对话轮次，无法适配模型回复的动态变化，难以捕捉对话过程中偏见的动态演变特征，漏检风险高。
### 方法关键点
提出DyMT-ESB受控评估协议，可基于实时更新的对话历史动态生成用户后续查询，支持可变轮次的多轮交互偏见检测，实现逐轮追踪偏见表现。
### 关键结果
实验验证LLM在连贯、响应自适应的多轮交互中仍会释放社会偏见，明确三类未被传统评估覆盖的偏见模式：1）晚现偏见：长对话后期才首次出现偏见；2）非单调偏见：偏见程度随轮次上下波动，无固定变化趋势；3）偏见复现：已消失的偏见在后续轮次再次出现，传统固定轮次预脚本评估对以上模式的漏检率极高。
