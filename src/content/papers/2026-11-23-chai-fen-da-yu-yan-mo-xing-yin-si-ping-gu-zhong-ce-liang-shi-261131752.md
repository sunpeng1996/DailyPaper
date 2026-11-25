---
title: Separating Measurement Failures from Defence Failures in Split Language-Model
  Privacy
title_zh: 拆分大语言模型隐私评估中测量失效与防御失效的区分方法
authors:
- Georgios Politis
- Evangelos Pappas
affiliations:
- Setloop.io
arxiv_id: '2611.31752'
url: https://arxiv.org/abs/2611.31752
pdf_url: https://arxiv.org/pdf/2611.31752
published: '2026-11-23'
collected: '2026-11-25'
category: Eval
direction: 拆分LLM · 隐私评估框架
tags:
- Split-LLM
- Privacy Evaluation
- Calibrated Probe
- Split Training
- Privacy Defence
one_liner: 提出拆分LLM隐私评估失效模式分类框架，通过校准探针统一隐私泄露判定标准
practical_value: '- 部署端侧+云端Split LLM做推荐/Agent推理时，先校准攻击探针再验证隐私防御效果，避免无效探针导致的误判

  - 做拆分训练隐私评估时需区分测量失效和防御失效，不要把探针未校准等问题误判为防御有效

  - 依赖变分互信息下界接近0的结论不能直接证明无隐私泄露，需补充最坏场景的泄露校验'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有拆分LLM隐私评估常混淆测量失效（如探针未校准、忽略梯度通道等）与防御失效，导致结论可信度低，无法准确判定隐私防御方案的真实有效性。
### 方法关键点
- 定义5类评估主张可采纳状态：泄露、未检测、覆盖未确定、测量无效、超范围推理
- 对4个拆分LLM评估项目、2项跨范围校验（主机密钥托管、变分互信息界）做回溯证据重分析
- 建立探针校准准入标准，仅保留符合要求的探针结果作为判定依据
### 关键结果数字
19组配置探索中仅4/24探针合格，合格探针在13组配置中验证到合规隐私泄露；7组防御重测试验中，所有配置的下一字节结构探针突破0.02阈值（范围0.097-0.112），标点属性探针准确率达0.79-0.89，最终4组防御明确失效、3组评估结果未确定；共享密钥正交包装仅能防护被动网络捕获，无法对抗被攻破的恢复主机，近零变分下界无法约束最坏情况信息泄露。
