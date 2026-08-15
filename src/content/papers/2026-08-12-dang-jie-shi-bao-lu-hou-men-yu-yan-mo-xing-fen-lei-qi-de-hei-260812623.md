---
title: 'When Explanations Betray Backdoors: Black-Box Auditing for Language Model
  Classifiers'
title_zh: 当解释暴露后门：语言模型分类器的黑盒审计方法
authors:
- Yang Liu
- Ran Zou
affiliations:
- University of North Carolina at Chapel Hill
- University of California, Irvine
arxiv_id: '2608.12623'
url: https://arxiv.org/abs/2608.12623
pdf_url: https://arxiv.org/pdf/2608.12623
published: '2026-08-12'
collected: '2026-08-15'
category: LLM
direction: LLM安全 · 后门黑盒检测
tags:
- Backdoor Detection
- Black-box Auditing
- LLM Classifier
- Groundedness Evaluation
- Safety Audit
one_liner: 提出轻量Groundedness Drift得分，黑盒无触发信息场景下高效检测LLM分类器的后门攻击
practical_value: '- 电商内容审核、用户评论分类、商品标签打标等场景使用的LLM分类器，可直接复用Groundedness Drift得分做后门检测，无需已知攻击触发词，仅需少量干净校准数据即可快速落地

  - 对要求输出可解释性的LLM分类服务，可将groundedness一致性校验加入上线前安全审计流程，大幅降低模型被投毒植入后门的风险

  - 高风险合规场景（如广告合规审核、敏感内容识别）可搭配多探针Unsupported Groundedness方案作为补充校验，提升伪装后门的检出率'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
带解释输出的LLM分类器广泛用于内容审核、主题分流、低资源标注等场景，但后门攻击难被传统验证流程发现，现有检测方法大多依赖已知触发词信息，黑盒无触发信息场景下缺少高效审计方案。
### 方法关键点
1. 设计轻量Groundedness Drift得分，衡量LLM分类输出的标签+解释与输入的一致性，无需知晓后门触发词，仅需干净校准数据即可实现黑盒检测
2. 针对解释伪装的极端场景，提出多探针的Unsupported Groundedness升级方案，进一步强化检测信号
### 关键结果数字
在2款7B基座、5个数据集、4类OpenBackdoor主流非自适应攻击的测试集上，5%干净样本假阳率约束下，Groundedness Drift的AUROC高于所有对比检测器，残留目标攻击成功率（ASR）为所有方案最低；Unsupported Groundedness可进一步提升检测信号，但仍无法完全覆盖自适应攻击场景
