---
title: 'Certify or Refuse: A Cross-Model Map for Selective Risk Control with Coverage
  Floors under Covariate Shift'
title_zh: 协变量偏移下带覆盖率下限的选择性风险控制跨模型映射
authors:
- Jiamiao Liu
- Dewen Qiao
- Yu Zhang
- Xuetao Chen
affiliations:
- Xinqiao Hospital
- Army Medical University (Third Military Medical University)
arxiv_id: '2608.10893'
url: https://arxiv.org/abs/2608.10893
pdf_url: https://arxiv.org/pdf/2608.10893
published: '2026-08-11'
collected: '2026-08-12'
category: Eval
direction: 模型风险评估 · 分布偏移鲁棒性
tags:
- Covariate Shift
- Selective Prediction
- Risk Control
- Distribution Robustness
- Certification
one_liner: 给出协变量偏移下带覆盖率下限的选择性风险控制跨模型映射及可落地的风险认证上下界
practical_value: '- 电商大促、新用户涌入等分布偏移场景下，可引入带β覆盖率下限的选择性预测框架，同时满足bad case率α控制、自动化处理比例不低于业务要求

  - 多模型路由场景可复用跨模型认证思路：用源域标注数据控风险，目标域无标注数据控覆盖率，大幅降低新场景标注成本

  - 可实现的Model-B''上界方法可直接用于LLM Agent、生成式推荐的输出准入校验，避免无差别拒答损伤用户体验'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有选择性风险认证方法仅关注错误率控制，无法满足业务对最低自动化处理比例的硬性要求，且未考虑协变量偏移（分布变化）场景下的认证有效性。
### 方法关键点
基于有界比率协变量偏移假设，Floor Certification Map跨模型框架将认证复杂度拆解为两部分：源域标注数据承担错误率α的认证成本，目标域无标注数据承担覆盖率下限β的认证成本；给出三类模型结果：下界Model-B、匹配的神谕权重上界Model-A、可落地的上界Model-B'，证明单模型无法在全偏移类下实现最优匹配。
### 关键结果数字
1024-cell审计未出现正式认证触发后的违规情况；SQuAD到NewsQA的跨域审计实现可信拒答；注册bite族对数对数斜率为-2.002，符合理论预期
