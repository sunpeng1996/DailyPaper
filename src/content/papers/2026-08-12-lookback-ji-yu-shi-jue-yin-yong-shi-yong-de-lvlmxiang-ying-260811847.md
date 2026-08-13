---
title: 'LookBack: Where and How to Score LVLM Responses via Visual Reference Usage'
title_zh: LookBack：基于视觉引用使用的LVLM响应打分方法
authors:
- Beomsik Cho
- Jinhyeong Kim
- Dongseok Lee
- Jaehyung Kim
affiliations:
- Yonsei University
arxiv_id: '2608.11847'
url: https://arxiv.org/abs/2608.11847
pdf_url: https://arxiv.org/pdf/2608.11847
published: '2026-08-12'
collected: '2026-08-13'
category: Eval
direction: 多模态大模型 · 响应质量评估
tags:
- LVLM
- Response Scoring
- Hallucination Mitigation
- Best-of-N
- Training-free
one_liner: 提出免训练的LookBack方法，结合token似然与视觉引用强度提升LVLM响应Best-of-N选择效果
practical_value: '- 电商多模态商品问答（如直播导购、详情页智能问答）场景可直接集成LookBack做响应筛选，规避LVLM说错商品属性、款式的视觉幻觉问题，无需额外训练

  - 多模态生成式推荐的推荐理由生成环节，可通过LookBack校验生成文案和商品主图/详情图的一致性，提升生成内容可信度，额外开销极低

  - 多模态导购Agent的输出校验层可接入LookBack，确保给用户推送的图文推荐响应中文案与配图匹配，降低因信息错配导致的客诉'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LVLM同时存在文本幻觉与视觉幻觉，生成的响应流畅但可能完全不符合输入图像内容；现有从LLM迁移来的置信度打分仅衡量文本合理性，无法校验响应与输入图像的一致性，实验显示移除输入图像后置信度打分结果几乎无变化，完全不适配多模态场景的响应质量判别需求。
### 方法关键点
LookBack是完全免训练的LVLM响应打分方案：在原有token生成似然的基础上，新增轻量的视觉回视得分，衡量每个生成token对图像token的引用强度，两者加权结合作为最终的响应质量打分。视觉回视得分通过计算生成token与图像特征的注意力权重关联度得到，无需微调模型，可直接嵌入现有LVLM推理流程。
### 关键结果
在4个公开基准、3款主流LVLM上的测试显示，LookBack在Best-of-N选择任务上全方位优于现有置信度基线，仅增加可忽略的推理延迟
