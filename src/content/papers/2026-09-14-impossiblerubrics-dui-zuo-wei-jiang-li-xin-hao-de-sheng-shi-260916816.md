---
title: 'ImpossibleRubrics: Stress-Testing Generated Rubrics as Reward Signals'
title_zh: 《ImpossibleRubrics：对作为奖励信号的生成式评分规则的压力测试》
authors:
- Bowen Qin
- Yi Xie
- Yesheng Liu
- Xi Yang
affiliations:
- National University of Singapore
- Peking University
- Institute of Automation, Chinese Academy of Sciences
- JD.com
arxiv_id: '2609.16816'
url: https://arxiv.org/abs/2609.16816
pdf_url: https://arxiv.org/pdf/2609.16816
published: '2026-09-14'
collected: '2026-09-16'
category: Eval
direction: 生成式评分规则·奖励信号鲁棒性评估
tags:
- rubric_generation
- reward_hacking
- LLM_as_judge
- adversarial_evaluation
- benchmark
one_liner: 构建含169个不可完成任务的基准，测试生成式评分规则作为奖励信号的被攻击漏洞
practical_value: '- 搭建LLM-as-Judge自动评估链路时，可参考本文的对抗压力测试流程，针对业务场景构造证据受限的负样本，提前发现评分规则的漏洞，避免生成的推荐文案/客服回复为拿高分编造事实误导用户

  - 业务中使用生成式rubric作为RLHF的奖励信号时，可加入「奖励证据忠实性、惩罚过度断言」的显式prompt约束，本文实测该方法可降低13%-18%的被攻击率

  - 做电商商品/内容的生成式评价、回复自动打分时，不要只依赖单个LLM的校验结果，不同Oracle配置下的违规判定率差异可达42个百分点，建议做多模型交叉校验+人工抽样校准'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
生成式评分规则（rubric）目前已被广泛应用于RLHF奖励信号、LLM-as-Judge自动评估、生成内容自动打分等场景，但这类规则存在明显的被攻击漏洞：对抗性回答可通过满足所有rubric条目但违反真实业务目标拿到高分，尤其在证据不足需要诚实拒答的场景下，这类漏洞会直接导致生成内容偏离事实、误导用户，现有基准缺乏对这类场景的针对性测试。
### 方法关键点
- 构建ImpossibleRubrics基准：包含169个跨6类的证据受限不可完成任务、48个可回答对照任务，每个任务配套封闭证据包和可机器校验的合规证书，不预置固定评分规则，支持任意rubric生成器的压力测试
- 标准化评估流程：生成器基于任务+证据生成rubric→固定攻击模型针对性生成最大化rubric得分的回答→裁判模型盲测对比攻击回答与诚实基线的得分→Oracle校验攻击回答是否违反合规证书，满足「攻击得分≥基线+违规」即判定rubric被利用
### 关键结果
固定攻击、裁判、Oracle配置下测试11款主流LLM生成器：无偏Full-150集上被利用率为8%~26%；高难度Hard-45压力集上最低为36%，最高可达98%，而人工编写的符合证书要求的rubric被利用率为0%。仅更换Oracle校验模型时，同一测试集的被利用率可在33.3%~75.6%之间波动，结果一致性受校验规则影响极大。
> 最值得记住的一句话：生成式评分规则的漏洞率统计必须和校验规则、基线审计、敏感性分析一起披露，否则不具备业务参考价值
