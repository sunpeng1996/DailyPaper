---
title: 'Ventor-QTest: Threat-Model-Driven Verification of Vendor-Hosted LLM APIs'
title_zh: Ventor-QTest：面向厂商托管LLM API的威胁模型驱动黑盒验证工具
authors:
- Xiangfan Wu
- Zonghao Ying
- Huiyu Wu
- Xing Zheng
- Huangsheng Cheng
- Xiaorong Shi
- Jing Guo
affiliations:
- Tencent Zhuque Lab
arxiv_id: '2608.16391'
url: https://arxiv.org/abs/2608.16391
pdf_url: https://arxiv.org/pdf/2608.16391
published: '2026-08-16'
collected: '2026-08-18'
category: LLM
direction: LLM API 黑盒审计 · 行为一致性验证
tags:
- LLM API
- Black-box Audit
- Fidelity Loss
- Behavioral Consistency
- Threat Model
one_liner: 提出双指标黑盒审计方案，无需目标API输出概率即可检测托管LLM API与可信参考的行为偏差
practical_value: '- 若业务依赖第三方LLM API做推荐文案生成、电商导购Agent推理，可直接复用AFL+EFL双指标方案定期审计API一致性，避免厂商偷偷降精度、换模型导致业务效果波动

  - 长链路Agent任务（如自动化投放、多轮导购）重点监控EFL指标，实验显示EFL升高会导致长horizon任务通过率显著下降，比平均指标对业务风险的感知更敏感

  - 可复用重复请求拟合输出分布、参考端重打分计算中心惊奇度的工程实现，无需目标API开放logprob，仅通过文本输出即可完成审计，适配绝大多数商用LLM API

  - 多厂商LLM调用层可嵌入该工具做实时流量校验，拦截行为偏差过大的厂商请求，降低生成内容质量不稳定、Agent推理失败等业务风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前开源大模型部署硬件门槛高，大量业务依赖第三方托管LLM API，但厂商可能存在未告知的低精度量化、旧版本复用、路由到廉价模型等行为，API返回的模型标识无可信背书；现有审计方案要么需要目标API开放logprob权限，要么仅能检测平均偏差，漏检间歇性极端偏差，严重影响生成式推荐、长链路Agent等业务的稳定性。
### 方法关键点
- 设计双指标审计框架：① 平均保真损失（AFL）：对固定上下文重复请求M次，拟合目标输出分类分布，用零偏校正的粗粒度KL散度衡量与可信参考分布的平均偏差；② 极端保真损失（EFL）：独立生成多组长序列，通过参考端重打分的中心惊奇度上尾分布衡量极端偏差，两个指标独立报告不合并为单一阈值
- 仅需可信参考端提供logprob，目标API仅需返回普通文本，无额外权限要求
- 覆盖5级威胁模型，适配从正常运维偏差到自适应路由作弊的全场景检测
### 关键结果
- 测试7个DeepSeek V4 Flash托管路由，官方自检测AFL接近0，其余6个第三方路由均显著偏离参考分布，AFL最高达0.57
- AFL与logprob导出的粗粒度KL散度Pearson相关系数达0.971，一致性极强
- EFL与GPQA-Diamond准确率无明显关联，但EFL最高的DigitalOcean路由，长链路Terminal-Bench任务通过率从低任务暴露组的82.6%降至高暴露组的13.6%
### 核心结论
平均偏差指标无法反映间歇性极端保真损失，长链路Agent类任务的稳定性对EFL更敏感，需同时监控AFL和EFL两个指标
