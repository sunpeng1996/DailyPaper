---
title: 'PMRecBench: A Benchmark for Personalization in Recommendation Agents under
  Multimodal Queries'
title_zh: PMRecBench：多模态查询下推荐Agent个性化能力评估基准
authors:
- Xiaoyu Zhang
- Yougang Lyu
- Bin Wu
- Sahan Bulathwela
- Emine Yilmaz
affiliations:
- University College London
- University of Amsterdam
arxiv_id: '2611.06349'
url: https://arxiv.org/abs/2611.06349
pdf_url: https://arxiv.org/pdf/2611.06349
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: 推荐Agent评估 · 多模态查询个性化
tags:
- Recommendation Agent
- Multimodal Query
- Personalization
- Benchmark
- Preference Following
one_liner: 首个结合真实用户历史的多模态查询推荐Agent个性化基准，揭示偏好遵从度下降问题
practical_value: '- 做多模态搜推Agent时，可复用诊断池设计拆分「需求理解」和「偏好遵从」两个能力维度，避免仅用全局NDCG掩盖个性化不足问题

  - 多模态输入会挤占Agent对用户历史偏好的注意力，工程实现时可增加偏好信号加权模块，或在推理阶段显式要求Agent先匹配需求再按偏好重排

  - 不要盲目升级商用MLLM backbone解决个性化问题，实验显示商用模型需求理解接近天花板但偏好遵从度反而低于Gemma-4-31B，可优先优化排序逻辑而非单纯换大模型'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前电商、内容平台已广泛支持图文结合的多模态推荐查询，但现有评估基准存在明显缺陷：纯文本个性化基准不支持多模态输入，多模态检索基准仅验证需求匹配度，不结合真实用户交互历史评估个性化能力，无法诊断推荐Agent在多模态输入下是否能平衡「满足当前查询需求」和「遵从用户历史偏好」两个核心目标。
### 方法关键点
- 构建510条质量受控的图文多模态查询，覆盖服饰、电影两个品类，每条查询绑定对应用户的真实交互历史，查询需求从用户历史行为的一致模式挖掘，参考图像均来自用户真实交互过的物品，避免查询需求和用户偏好天然冲突。
- 设计诊断候选池：除同时满足需求和偏好的目标物品外，加入两类干扰项：符合用户偏好但违反查询需求的物品、符合查询需求但不符合用户偏好的物品，对应提出U（需求理解得分）、P（偏好遵从得分）两个独立评估指标，拆分两类能力的表现。
### 关键实验结果
在Amazon服饰、MovieLens两个公开数据集上测试4类共12种推荐方法+8款不同规模MLLM backbone：① 加入多模态查询后，4个主流Agent的偏好遵从度P平均下降4~8个百分点，但全局NDCG反而提升，暴露「需求匹配提升但个性化下降」的失衡问题；② 商用MLLM的需求理解得分U可达0.9~0.93接近天花板，但偏好遵从度P比Gemma-4-31B低5~8个百分点，单纯升级模型无法解决失衡。
### 核心结论
多模态输入会让推荐Agent优先关注物品与参考图像的相似度，挤占对用户历史偏好的注意力，仅靠提升模型规模无法解决该问题，需显式设计偏好加权逻辑
