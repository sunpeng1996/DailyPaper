---
title: 'Pterodactyl: Pushing the Limits of Efficient Automated Translation Evaluation'
title_zh: Pterodactyl：高效自动翻译评估的极限优化方案
authors:
- Evelyn Y. Garland
- Carola F. Berger
affiliations:
- 1020 Group
- Acta Language Services, LLC
- CFB Scientific Translations LLC
arxiv_id: '2611.14480'
url: https://arxiv.org/abs/2611.14480
pdf_url: https://arxiv.org/pdf/2611.14480
published: '2026-11-10'
collected: '2026-11-12'
category: Eval
direction: 大模型自动评估 · 成本性能优化
tags:
- LLM-as-judge
- Evaluation
- Prompt Engineering
- Cost Optimization
- Binary Classification
one_liner: 推出低成本可定制LLM-as-judge翻译评估系统，在WMT26两项子任务实现最优性价比
practical_value: '- 做生成式推荐文案、Agent回答、RAG结果的质量评估时，可复用ROC分析指导prompt工程与模型选型，同性能下优先选低成本小模型，降低推理开销

  - 针对二分类质检场景（如广告合规校验、UGC内容质量筛除），可参考「先找通用筛选阈值、避免各组件单独调优」的思路，缩短迭代周期

  - 生产上线多候选方案选型时，优先对齐成本、延迟指标，不用盲目追求大参数模型，保障高吞吐场景的可用性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有基于LLM-as-judge的无参考翻译质量评估方案开发部署复杂度高、推理成本高，无法适配生产环境高吞吐、低开销的需求。
### 方法关键点
1. 基于LLM-as-judge框架搭建，全程用ROC分析指导prompt优化、模型选型流程，避免无效的独立组件调优
2. 针对片段级质量打分、无错片段检测两个场景定制模型变体，核心面向二分类的翻译分流、数据标注场景做性能优化
3. 同等性能表现下优先选择token消耗少、推理速度快的方案，最大化压缩部署与运行成本、降低延迟
### 关键结果
系统具备高定制性、极低运行成本的特性，在WMT26两项翻译评估子任务上达到成本-性能前沿水平，不同测试场景下鲁棒性表现稳定
